from researchos.cli import main


def test_status(capsys):
    assert main(["status"]) == 0
    assert "alpha" in capsys.readouterr().out


def test_project_scaffold(tmp_path):
    args = ["init-project", "Test Study", "--type", "empirical", "--root", str(tmp_path)]
    assert main(args) == 0
    assert (tmp_path / "test-study" / "protocol" / "research_charter.md").exists()
    assert main(args) == 2
