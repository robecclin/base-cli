from tests.conftest import RunCli


def test_hello(run_cli: RunCli) -> None:
    result = run_cli("hello")
    assert result.exit_code == 0
    assert result.stdout == "Hello, world!\n"
    assert result.stderr == ""


def test_hello_with_name(run_cli: RunCli) -> None:
    result = run_cli("hello", "--name", "Alice")
    assert result.exit_code == 0
    assert result.stdout == "Hello, Alice!\n"
    assert result.stderr == ""


def test_goodbye(run_cli: RunCli) -> None:
    result = run_cli("goodbye")
    assert result.exit_code == 0
    assert result.stdout == "Goodbye, world!\n"
    assert result.stderr == ""


def test_goodbye_with_name(run_cli: RunCli) -> None:
    result = run_cli("goodbye", "--name", "Bob")
    assert result.exit_code == 0
    assert result.stdout == "Goodbye, Bob!\n"
    assert result.stderr == ""


def test_no_subcommand(run_cli: RunCli) -> None:
    result = run_cli()
    assert result.exit_code == 2
    assert "Usage:" in result.stdout
    assert "hello" in result.stdout
    assert "goodbye" in result.stdout
    assert result.stderr == ""


def test_unknown_subcommand(run_cli: RunCli) -> None:
    result = run_cli("unknown")
    assert result.exit_code == 2
    assert result.stdout == ""
    assert "No such command 'unknown'." in result.stderr


def test_help(run_cli: RunCli) -> None:
    result = run_cli("--help")
    assert result.exit_code == 0
    assert "hello" in result.stdout
    assert "goodbye" in result.stdout
    assert result.stderr == ""
