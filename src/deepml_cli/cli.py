import argparse
from pathlib import Path

from deepml_cli.fetch import fetch_problem


def build_parser():
    parser = argparse.ArgumentParser(
        prog="deepml",
        description="DeepML CLI Tool",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sync command
    fetch_parser = subparsers.add_parser(
        "fetch", help="Fetch a question from Open-Deep-ML"
    )
    fetch_parser.add_argument(
        "question_number", type=int, help="Question number to fetch (required)"
    )
    fetch_parser.add_argument(
        "-d",
        "--dest-dir",
        type=Path,
        default=Path.cwd(),
        help="Destination directory (default: current directory)",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "fetch":
            args.dest_dir.mkdir(parents=True, exist_ok=True)
            fetch_problem(args.question_number, args.dest_dir)
        else:
            parser.print_help()

    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()
