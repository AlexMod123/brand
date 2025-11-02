import pytest
from src.data_loader import DataLoader
from src.make_report import AverageRatingReport

@pytest.fixture
def sample_data():
    return [
        {"name": "iphone 15 pro", "brand": "apple", "price": 999.0, "rating": 4.9},
        {"name": "galaxy s23 ultra", "brand": "samsung", "price": 1199.0, "rating": 4.8},
        {"name": "iphone 14", "brand": "apple", "price": 799.0, "rating": 4.8},
        {"name": "galaxy a54", "brand": "samsung", "price": 449.0, "rating": 4.7},
    ]

def test_average_rating(sample_data):
    report = AverageRatingReport()
    result = report.generate(sample_data)

    assert len(result) == 2
    assert result[0]["Brand"] == "Apple"
    assert result[0]["Rating"] == 4.85
    assert result[1]["Brand"] == "Samsung"
    assert result[1]["Rating"] == 4.75

def test_load_multiple_files(tmp_path):
    # Создаём временные файлы
    f1 = tmp_path / "f1.csv"
    f1.write_text("name,brand,price,rating\niphone,apple,999,4.9\ngalaxy,samsung,1199,4.8\n")

    f2 = tmp_path / "f2.csv"
    f2.write_text("name,brand,price,rating\npixel,google,699,4.7\nredmi,xiaomi,199,4.6\n")

    data = DataLoader.load_files([str(f1), str(f2)])
    assert len(data) == 4
    assert any(row["brand"] == "apple" for row in data)