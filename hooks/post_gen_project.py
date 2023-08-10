import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(dirpath) -> None:
    os.rmdir(os.path.join(PROJECT_DIRECTORY, dirpath))


def remove_multiple_files(*files) -> None:
    for file in files:
        remove_file(file)


def main():
    if not {{cookiecutter.docker}}:
        remove_multiple_files("Dockerfile", ".dockerignore")
    if not {{cookiecutter.alembic}}:
        remove_dir("migrations")
        remove_file("alembic.ini")


if __name__ == "__main__":
    main()
