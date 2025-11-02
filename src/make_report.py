from typing import List, Dict, Protocol
from collections import defaultdict

class Report(Protocol):
    name: str

    def generate(self, data: List[Dict]) -> List[Dict]:
        ...

class AverageRatingReport:
    name = "average-rating"

    def generate(self, data: List[Dict]) -> List[Dict]:
        brand_ratings = defaultdict(list)

        for row in data:
            brand = row["brand"].strip().lower()
            rating = row["rating"]
            brand_ratings[brand].append(rating)

        result = []
        for brand, ratings in brand_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            result.append({"Brand": brand.capitalize(), "Rating": round(avg_rating, 2)})

        return sorted(result, key=lambda x: x["Rating"], reverse=True)