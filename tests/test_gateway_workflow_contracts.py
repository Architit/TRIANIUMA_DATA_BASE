# Copyright (c) 2026-06-07 RADRILONIUMA / TRIANIUMA Kingdom. All rights reserved.
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_gateway_script_contract_present():
    script = (REPO_ROOT / "scripts" / "gateway_io.sh").read_text(encoding="utf-8")
    assert "verify_github" in script
    assert "verify_onedrive" in script
    assert "verify_gworkspace" in script
    assert "do_export" in script
    assert "do_import" in script
    assert "Usage: $0 [verify|export|import <archive>]" in script


def test_workflow_snapshot_state_references_contract_layers():
    text = (REPO_ROOT / "WORKFLOW_SNAPSHOT_STATE.md").read_text(encoding="utf-8")
    assert "WORKFLOW_SNAPSHOT_CONTRACT.md" in text
    assert "SYSTEM_STATE_CONTRACT.md" in text
