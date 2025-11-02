import argparse

def ParseArgs():
    parser = argparse.ArgumentParser(description="Brand rating analysis tool")
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files with product data"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=["average-rating"],
        help="Type of report to generate"
    )
    return parser.parse_args()