import tempfile

import nox


def install_with_constraints(
    session: nox.Session,
    *args: str,
    **kwargs: str,
) -> None:
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session
def lint(session: nox.Session) -> None:
    session.install("pre-commit")
    session.install("wemake-python-styleguide")
    session.install("Flake8-pyproject")
    session.run("pre-commit", "run", "--all-files")


@nox.session
def test(session: nox.Session) -> None:
    args = session.posargs or ["-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("poetry", "run", "task", "test", *args)
