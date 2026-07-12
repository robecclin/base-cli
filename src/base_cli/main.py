from base_cli.app import app
from base_cli.command.goodbye import goodbye
from base_cli.command.hello import hello

__all__ = ["app", "goodbye", "hello"]

if __name__ == "__main__":
    app()  # pragma: no cover
