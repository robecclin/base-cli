# Base CLI

Minimal CLI template with latest tooling and strict checks.

## Usage

Print a hello world greeting:

```sh
$ uv run base-cli hello --name Alice
Hello, Alice!
```

Print a goodbye farewell:

```sh
$ uv run base-cli goodbye --name Bob
Goodbye, Bob!
```

## Development

```sh
make install # uv sync --locked
make check   # ruff, vulture, ty, pyright, mypy, pytest+coverage, yamllint
make upgrade # uv sync --upgrade
make clean   # remove caches
```
