
FROM python:3.10.10 as base

RUN pip install poetry

WORKDIR /code

COPY poetry.lock pyproject.toml .

RUN poetry config virtualenvs.create false && poetry -vvv install --no-root

COPY . .


RUN pip install nox==2023.4.22 && \
  nox -s test -- -m "not smoke"

CMD python -m {{ cookiecutter.package }}.main
