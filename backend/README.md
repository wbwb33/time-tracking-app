# Time Tracking Backend

## Backend Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

## Backend local development

Start with Docker Compose:

```bash
sh start-dev.sh
```

Now you can open your browser and interact with these URLs:

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost/docs

PGAdmin, PostgreSQL web administration: http://localhost:5050

## Backend tests

To test the backend run:

```bash
sh start-test.sh
```