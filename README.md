# pytest-path

Example project for setting up [pytest](https://docs.pytest.org/) with your source code inside `src` folder and tests inside `tests` folder.

This repo also has an example of how to run [pytest](https://docs.pytest.org/) using [tox](https://tox.wiki/) in [Github Actions](https://github.com/ianpogi5/pytest-path/actions).

[![test](https://github.com/ianpogi5/pytest-path/actions/workflows/test.yml/badge.svg)](https://github.com/ianpogi5/pytest-path/actions/workflows/test.yml)

## Development

```bash
git clone git@github.com:ianpogi5/pytest-path.git
cd pytest-path
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Testing

Run `pytest` on time.

```bash
pytest
```

or you can run `pytest` every time you change a file.

```bash
ptw
```

## Running locally

Install your package locally

```bash
pip install -e .
```

Run the program

```bash
python -m coffee latte
```
