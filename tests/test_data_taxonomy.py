from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _has_any(patterns):
    for pattern in patterns:
        if list(REPO_ROOT.glob(pattern)):
            return True
    return False


def test_root_taxonomy_surfaces_exist():
    assert _has_any(["LAM_MEM*.txt", "LAM_MEM*.*.txt"]), "missing memory artifacts"
    assert _has_any(["*VECTOR*.txt"]), "missing vector artifacts"
    assert _has_any(["INT.*.txt"]), "missing incident artifacts"
    assert _has_any(["file tasks*.txt", "*tasks-*.docx"]), "missing task artifacts"
    assert _has_any(["*core.py.txt"]), "missing code prototype artifacts"


def test_workflow_onedrive_contains_txt_payloads():
    onedrive = REPO_ROOT / "Workflows" / "Onedrive"
    assert onedrive.exists(), "missing Workflows/Onedrive"
    txt_files = list(onedrive.rglob("*.txt"))
    assert txt_files, "no txt payloads under Workflows/Onedrive"
