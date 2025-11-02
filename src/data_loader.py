import csv
from typing import List, Dict

class DataLoader:
    @staticmethod
    def load_files(file_paths: List[str]) -> List[Dict]:
        data = []
        for path in file_paths:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Преобразуем rating в float
                    row['rating'] = float(row['rating'])
                    row['price'] = float(row['price'])
                    data.append(row)
        return data