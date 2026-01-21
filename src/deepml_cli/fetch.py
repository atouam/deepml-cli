from pathlib import Path

import requests

# Default URL constants
BUILD_TEMPLATE_URL = "https://raw.githubusercontent.com/Open-Deep-ML/DML-OpenProblem/refs/heads/main/build/{question_number}.json"


def fill_starter_code(file_path: Path, starter_code: str, test_cases: list):
    """Fill the starter code file with the provided starter code and test cases."""
    with file_path.open("w", encoding="utf-8") as f:
        f.write(starter_code)
        f.write("\n\n# Test Cases\n")
        for i, test_case in enumerate(test_cases):
            f.write(f"# Test Case {i + 1}\n")
            f.write(f"{test_case['test']}\n")
            f.write(f"print({test_case['expected_output']})\n\n")


def fetch_problem(question_number: int, dest_dir: Path):
    """Fetch the problem build file and create starter code files."""
    if dest_dir.exists() and not dest_dir.is_dir():
        raise ValueError(f"Destination {dest_dir} exists and is not a directory.")

    url = BUILD_TEMPLATE_URL.format(question_number=question_number)
    response = requests.get(url)
    response.raise_for_status()
    build_file = response.json()

    problems_name = build_file.get("title").replace(" ", "-").lower()
    dest_dir = dest_dir / problems_name
    dest_dir.mkdir(parents=True, exist_ok=False)

    # numpy
    if "starter_code" in build_file and "test_cases" in build_file:
        fill_starter_code(
            dest_dir / "solution_numpy.py",
            build_file.get("starter_code", ""),
            build_file.get("test_cases", []),
        )

    # pytorch
    if "pytorch_starter_code" in build_file and "pytorch_test_cases" in build_file:
        fill_starter_code(
            dest_dir / "solution_pytorch.py",
            build_file.get("pytorch_starter_code", ""),
            build_file.get("pytorch_test_cases", []),
        )

    # tinygrad
    if "tinygrad_starter_code" in build_file and "tinygrad_test_cases" in build_file:
        fill_starter_code(
            dest_dir / "solution_tinygrad.py",
            build_file.get("tinygrad_starter_code", ""),
            build_file.get("tinygrad_test_cases", []),
        )
