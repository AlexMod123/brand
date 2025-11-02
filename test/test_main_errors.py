import pytest
import sys
from src.main import main
import subprocess
from pathlib import Path
def test_main_errors():
    with pytest.raises(SystemExit):
        sys.argv = ["main.py", "--files", "nonexistent.csv"]
        main()

def test_main_import_error_specific_message():
    """Более точная проверка сообщения об ошибке"""
    result = subprocess.run(
        [sys.executable, "-m", "src.main", "--help"],
        capture_output=True,
        text=True,
    )
    
    # Если импорт сломан — даже --help не сработает
    if "ModuleNotFoundError" in result.stderr:
        assert "parse_cli" in result.stderr
        pytest.fail("Импорт в main.py сломан! Исправь: from .cli import parse_args")