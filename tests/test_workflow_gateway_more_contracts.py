# Copyright (c) 2026-06-07 RADRILONIUMA / TRIANIUMA Kingdom. All rights reserved.
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_gateway_access_contract_mentions_external_systems():
    text = (REPO_ROOT / "GATEWAY_ACCESS_CONTRACT.md").read_text(encoding="utf-8")
    assert "GitHub" in text
    assert "OneDrive" in text
    assert "Google Workspace" in text
    assert "scripts/gateway_io.sh verify" in text


def test_test_entrypoint_modes_declared():
    text = (REPO_ROOT / "scripts" / "test_entrypoint.sh").read_text(encoding="utf-8")
    assert "--all" in text
    assert "--governance" in text
    assert "--taxonomy" in text
    assert "--ci" in text


def test_onedrive_contains_lam_and_lram_branches():
    root = REPO_ROOT / "Workflows" / "Onedrive"
    assert (root / "LAM").exists(), "missing LAM branch under Workflows/Onedrive"
    assert (root / "LRAM").exists(), "missing LRAM branch under Workflows/Onedrive"
