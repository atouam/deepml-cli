# deepml-cli

A CLI tool for downloading machine learning practice problems from [Deep-ML](https://www.deep-ml.com).
Problem definitions are sourced from the [Open-Deep-ML/DML-OpenProblem](https://github.com/Open-Deep-ML/DML-OpenProblem) repo.
## Usage

```bash
uv run deepml fetch <question_number> --dest-folder ./questions
```

## Output

```text
questions/
└── <question-title>/
    ├── solution_numpy.py
    ├── solution_pytorch.py
    └── solution_tinygrad.py
```

Each `solution_*.py` file contains the starter code with test cases appended.

