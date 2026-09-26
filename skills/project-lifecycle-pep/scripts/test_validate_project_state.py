#!/usr/bin/env python3

import unittest

from validate_project_state import validate


def state() -> dict:
    return {
        "project": {"id": "p1", "scope_id": "main"},
        "lifecycle": {"state": "GENESIS"},
        "current_work": {
            "pep_stage": "discover",
            "required_gates": {"coverage": "NOT_CHECKED"},
        },
        "assets": [],
        "baseline": {
            "active_asset_id": None,
            "qualification": {
                "coverage": "NOT_CHECKED",
                "verify": "NOT_CHECKED",
                "validate": "NOT_CHECKED",
            },
        },
        "coverage": [],
    }


class ValidationTests(unittest.TestCase):
    def test_example_genesis_state_is_valid(self) -> None:
        self.assertEqual(validate(state()), [])

    def test_mature_requires_qualified_baseline(self) -> None:
        data = state()
        data["lifecycle"]["state"] = "MATURE"
        errors = validate(data)
        self.assertTrue(any("active Baseline" in error for error in errors))
        self.assertTrue(any("blocking qualifications" in error for error in errors))

    def test_cross_project_import_stays_candidate(self) -> None:
        data = state()
        data["assets"] = [
            {
                "id": "a1",
                "status": "Approved",
                "source_project_id": "another-project",
            }
        ]
        errors = validate(data)
        self.assertTrue(any("must remain Candidate" in error for error in errors))
        self.assertTrue(any("import_approved=true" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
