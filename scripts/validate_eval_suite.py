#!/usr/bin/env python3
"""Validate eval metadata and release-gate coverage without external packages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_DOMAINS = {"corporate-presentation", "sports-exhibition", "non-visual"}
REQUIRED_TOPICS = {
    "lifecycle",
    "baseline-continuation",
    "project-isolation",
    "handoff-bootstrap",
    "evidence-gate",
    "blocking",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cases_file", type=Path)
    args = parser.parse_args()
    try:
        suite = json.loads(args.cases_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}")
        return 1

    errors: list[str] = []
    cases = suite.get("cases", []) if isinstance(suite, dict) else []
    if not 10 <= len(cases) <= 20:
        errors.append(f"expected 10-20 cases, found {len(cases)}")

    ids: set[str] = set()
    domains: set[str] = set()
    topics: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"case {index} is not an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"case {index} has no id")
        elif case_id in ids:
            errors.append(f"duplicate id {case_id}")
        else:
            ids.add(case_id)
        domains.add(case.get("domain"))
        topics.update(case.get("topics", []))
        for field in ("title", "scenario", "expected", "assertions", "skills"):
            if not case.get(field):
                errors.append(f"{case_id or index} missing {field}")

    missing_domains = REQUIRED_DOMAINS - domains
    missing_topics = REQUIRED_TOPICS - topics
    if missing_domains:
        errors.append(f"missing domains: {', '.join(sorted(missing_domains))}")
    if missing_topics:
        errors.append(f"missing topics: {', '.join(sorted(missing_topics))}")

    critical = set(suite.get("release_gate", {}).get("critical_cases", [])) if isinstance(suite, dict) else set()
    unknown_critical = critical - ids
    if unknown_critical:
        errors.append(f"unknown critical cases: {', '.join(sorted(unknown_critical))}")

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALID: {len(cases)} cases, {len(domains)} domains, {len(topics)} topics")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
