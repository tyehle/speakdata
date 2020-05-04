test:
    PYTHONPATH=src python3 -m pytest

type:
    mypy src tests

lint:
    flake8 src tests

format:
    black --line-length=79 src tests

check: test type lint format
