#!/usr/bin/env python3
"""Validate the small set of invariants that make PEP state safe to resume."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

LIFECYCLES = {"GENESIS", "CALIBRATION", "MATURE"}
PEP_STAGES = {"discover", "review", "freeze", "verify", "validate"}
ASSET_STATES = {"Candidate", "Approved", "Baseline", "Rejected"}
GATE_STATES = {"PASS", "FAIL", "NOT_CHECKED"}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate(data: object) -> list[str]:
    errors: list[str] = []
    require(isinstance(data, dict), "root must be an object", errors)
    if not isinstance(data, dict):
        return errors

    project = data.get("project")
    require(isinstance(project, dict), "project must be an object", errors)
    if isinstance(project, dict):
        require(bool(project.get("id")), "project.id is required", errors)
        require(bool(project.get("scope_id")), "project.scope_id is required", errors)

    lifecycle = data.get("lifecycle")
    require(isinstance(lifecycle, dict), "lifecycle must be an object", errors)
    state = lifecycle.get("state") if isinstance(lifecycle, dict) else None
    require(state in LIFECYCLES, f"lifecycle.state must be one of {sorted(LIFECYCLES)}", errors)

    current = data.get("current_work")
    require(isinstance(current, dict), "current_work must be an object", errors)
    stage = current.get("pep_stage") if isinstance(current, dict) else None
    require(stage in PEP_STAGES, f"current_work.pep_stage must be one of {sorted(PEP_STAGES)}", errors)
    gates = current.get("required_gates", {}) if isinstance(current, dict) else {}
    require(isinstance(gates, dict) and bool(gates), "current_work.required_gates must be a non-empty object", errors)
    if isinstance(gates, dict):
        for name, value in gates.items():
            require(value in GATE_STATES, f"current gate {name!r} has invalid state {value!r}", errors)
        if stage == "validate":
            blocked = [name for name, value in gates.items() if value != "PASS"]
            require(not blocked, f"validate is blocked by current gates: {', '.join(blocked)}", errors)

    assets = data.get("assets")
    require(isinstance(assets, list), "assets must be an array", errors)
    asset_by_id: dict[str, dict] = {}
    if isinstance(assets, list):
        for index, asset in enumerate(assets):
            require(isinstance(asset, dict), f"assets[{index}] must be an object", errors)
            if not isinstance(asset, dict):
                continue
            asset_id = asset.get("id")
            require(isinstance(asset_id, str) and bool(asset_id), f"assets[{index}].id is required", errors)
            if isinstance(asset_id, str) and asset_id:
                require(asset_id not in asset_by_id, f"duplicate asset id {asset_id!r}", errors)
                asset_by_id[asset_id] = asset
            require(asset.get("status") in ASSET_STATES, f"asset {asset_id!r} has invalid status", errors)
            if asset.get("source_project_id") and isinstance(project, dict) and asset.get("source_project_id") != project.get("id"):
                require(asset.get("status") == "Candidate", f"cross-project asset {asset_id!r} must remain Candidate", errors)
                require(asset.get("import_approved") is True, f"cross-project asset {asset_id!r} needs import_approved=true", errors)

    baseline = data.get("baseline")
    require(isinstance(baseline, dict), "baseline must be an object", errors)
    active_id = baseline.get("active_asset_id") if isinstance(baseline, dict) else None
    if active_id is not None:
        require(active_id in asset_by_id, "baseline.active_asset_id must reference an asset", errors)
        if active_id in asset_by_id:
            require(asset_by_id[active_id].get("status") == "Baseline", "active baseline asset must have Baseline status", errors)

    scope_id = project.get("scope_id") if isinstance(project, dict) else None
    baselines = [a for a in asset_by_id.values() if a.get("status") == "Baseline" and a.get("scope_id", scope_id) == scope_id]
    require(len(baselines) <= 1, "only one active Baseline is allowed per scope", errors)

    qualification = baseline.get("qualification", {}) if isinstance(baseline, dict) else {}
    require(isinstance(qualification, dict), "baseline.qualification must be an object", errors)
    if isinstance(qualification, dict):
        for name, value in qualification.items():
            require(value in GATE_STATES, f"baseline qualification {name!r} has invalid state {value!r}", errors)
    if state == "MATURE":
        require(bool(active_id), "MATURE requires an active Baseline", errors)
        required = {"coverage", "verify", "validate"}
        require(required.issubset(qualification), "MATURE requires coverage, verify, and validate qualifications", errors)
        blocked = [name for name in required if qualification.get(name) != "PASS"]
        require(not blocked, f"MATURE baseline has blocking qualifications: {', '.join(sorted(blocked))}", errors)

    coverage = data.get("coverage")
    require(isinstance(coverage, list), "coverage must be an array", errors)
    if isinstance(coverage, list):
        for index, case in enumerate(coverage):
            require(isinstance(case, dict), f"coverage[{index}] must be an object", errors)
            if isinstance(case, dict):
                require(bool(case.get("id")), f"coverage[{index}].id is required", errors)
                require(case.get("status") in GATE_STATES, f"coverage[{index}] has invalid status", errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state_file", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.state_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}")
        return 1
    errors = validate(data)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
