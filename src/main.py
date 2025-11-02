from .parse_cli import ParseArgs
from .data_loader import DataLoader
from .make_report import AverageRatingReport
from tabulate import tabulate

REPORT_REGISTRY = {
    "average-rating": AverageRatingReport()
}

def main():
    args = ParseArgs()

    if args.report not in REPORT_REGISTRY:
        raise ValueError(f"Unknown report: {args.report}")

    data = DataLoader.load_files(args.files)
    report = REPORT_REGISTRY[args.report]
    result = report.generate(data)

    print(tabulate(result, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()