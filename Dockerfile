FROM python:3.11

WORKDIR /app


COPY ./pyproject.toml ./poetry.lock ./

RUN pip install poetry

RUN poetry install --no-root --no-dev

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
