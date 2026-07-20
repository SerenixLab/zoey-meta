from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


TOOL_PATH = Path(__file__).with_name("zoey_governance.py")
SPEC = importlib.util.spec_from_file_location("zoey_governance", TOOL_PATH)
assert SPEC and SPEC.loader
GOVERNANCE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = GOVERNANCE
SPEC.loader.exec_module(GOVERNANCE)


class GovernanceProjectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.meta_root = TOOL_PATH.parents[2]

    def test_active_rule_source_closure_is_complete(self) -> None:
        standard = GOVERNANCE.load_artifact(self.meta_root, Path("ENGINEERING_STANDARD.md"))
        profile = GOVERNANCE.load_artifact(
            self.meta_root, Path("engineering/profiles/SCN001_SELECTED_SLICE.md")
        )
        integration = GOVERNANCE.load_artifact(
            self.meta_root, Path("engineering/integrations/codex/CODEX_INTEGRATION.md")
        )

        snapshots = GOVERNANCE.resolve_source_snapshots(
            self.meta_root, [standard, profile, integration]
        )
        self.assertEqual(
            {snapshot["id"] for snapshot in snapshots},
            {
                "OPEN_QUESTIONS",
                "ADR-001",
                "ADR-002",
                "ADR-003",
                "ADR-004",
                "ADR-005",
                "ADR-006",
                "ADR-007",
                "ADR-008",
                "ADR-009",
                "ADR-010",
                "ADR-011",
                "ADR-012",
            },
        )

    def test_projected_set_validates_and_initializes_complete_index(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory)
            arguments = type(
                "Arguments",
                (),
                {
                    "target": target,
                    "meta_root": self.meta_root,
                    "profile": ["engineering/profiles/SCN001_SELECTED_SLICE.md"],
                    "integration": ["engineering/integrations/codex/CODEX_INTEGRATION.md"],
                    "canonical_meta_source": "Zoey/meta",
                },
            )()

            GOVERNANCE.project(arguments)

            self.assertEqual(GOVERNANCE.validate_projection(target), [])
            self.assertEqual(GOVERNANCE.conformance_errors(target), [])
            self.assertEqual(GOVERNANCE.agent_routing_errors(target), [])
            lock = (target / "governance/ZOEY_GOVERNANCE.lock").read_text(encoding="utf-8")
            self.assertIn('"conformance_index"', lock)
            self.assertTrue((target / "AGENTS.md").exists())

    def test_conformance_rejects_stale_revision_and_duplicate_rows(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory)
            arguments = type(
                "Arguments",
                (),
                {
                    "target": target,
                    "meta_root": self.meta_root,
                    "profile": ["engineering/profiles/SCN001_SELECTED_SLICE.md"],
                    "integration": ["engineering/integrations/codex/CODEX_INTEGRATION.md"],
                    "canonical_meta_source": "Zoey/meta",
                },
            )()
            GOVERNANCE.project(arguments)

            conformance = target / "governance/CONFORMANCE.md"
            text = conformance.read_text(encoding="utf-8")
            row = next(line for line in text.splitlines() if line.startswith("| `ENG-"))
            stale = row.replace("| `R", "| `R999", 1)
            conformance.write_text(text.replace(row, stale, 1), encoding="utf-8")
            self.assertTrue(any(
                "revision mismatch" in error
                for error in GOVERNANCE.conformance_errors(target)
            ))

            conformance.write_text(text.replace(row, row + "\n" + row, 1), encoding="utf-8")
            self.assertTrue(any(
                "duplicate" in error
                for error in GOVERNANCE.conformance_errors(target)
            ))


if __name__ == "__main__":
    unittest.main()
