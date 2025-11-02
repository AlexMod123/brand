import sys
import subprocess
from pathlib import Path
import pytest
def test_main_no_files(tmp_path: Path):
    result = subprocess.run(
        [
            sys.executable,  "src.main",
            "--files", "nonexistent.csv",
            "--report", "average-rating"
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode != 0
    assert "No such file" in result.stderr or "FileNotFoundError" in result.stderr