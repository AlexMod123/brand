import subprocess
import sys
from pathlib import Path
import pytest

def test_main_average_rating_integration(tmp_path: Path):
    # --- 1. Создаём временные CSV-файлы ---
    csv1 = tmp_path / "products1.csv"
    csv1.write_text(
        "name,brand,price,rating\n"
        "iPhone 15,apple,999,4.9\n"
        "Galaxy S23,samsung,1199,4.8\n"
        "Redmi Note,xiaomi,199,4.6\n"
    )

    csv2 = tmp_path / "products2.csv"
    csv2.write_text(
        "name,brand,price,rating\n"
        "iPhone 14,apple,799,4.8\n"
        "Galaxy A54,samsung,449,4.7\n"
    )

    # --- 2. Запускаем main.py как отдельный процесс ---
    result = subprocess.run(
        [
            sys.executable, "-m", "src.main",
            "--files", str(csv1), str(csv2),
            "--report", "average-rating"
        ],
        capture_output=True,
        text=True,
    )

    # --- 3. Проверяем результат ---
    assert result.returncode == 0, f"Ошибка: {result.stderr}"

    output = result.stdout.strip()
    # Проверяем, что tabulate сработал
    assert "+----" in output  # grid-таблица
    assert "| Brand" in output
    assert "|   Rating" in output

    # Проверяем правильные значения
    lines = [line for line in output.splitlines() if "apple" in line.lower()]
    assert any("4.85" in line for line in lines)

    lines = [line for line in output.splitlines() if "samsung" in line.lower()]
    assert any("4.75" in line for line in lines)

    lines = [line for line in output.splitlines() if "xiaomi" in line.lower()]
    assert any("4.6" in line for line in lines)