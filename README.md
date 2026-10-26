# LeetCode Solutions in Python

My solutions to [LeetCode](https://leetcode.com/) problems written in Python.

## Project Structure

Each problem is implemented in a separate module with corresponding tests.

```text
solutions/
├── p0001_two_sum.py
├── p0002_add_two_numbers.py
└── ...
```

## Setup

Install dependencies using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Testing

Run all tests:

```bash
uv run pytest
```

Run tests for a specific problem:

```bash
uv run pytest tests/test_p0001_two_sum.py
```

## Code Quality

The project uses:

- **Ruff** — linting and formatting.
- **Mypy** — static type checking.
- **Pytest** — testing.
- **pre-commit** — automated checks before commits.
- **GitHub Actions** — continuous integration.

Run the linter:

```bash
uv run ruff check .
```

Check formatting:

```bash
uv run ruff format --check .
```

Run type checking:

```bash
uv run mypy .
```

Run all pre-commit hooks:

```bash
uv run pre-commit run --all-files
```
