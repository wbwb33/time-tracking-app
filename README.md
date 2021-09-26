# Time Tracking App

## Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.
* [Node](https://nodejs.org/en/download/).

## Local deployment

Before going further, make sure to create `.env` files from `.env.example`. Take note at these keys, it's important:
```
BACKEND_CORS_ORIGINS=["http://localhost:8888"]

BASE_URL=http://localhost
```
You have to make sure these two keys is right, based on where you deploy. If you deploy at server, please adjust these keys to the IP of the server.

Start with Docker Compose:

```bash
docker-compose up
```

Now you can open your browser and interact with these URLs:

Frontend (main app): http://localhost:8888

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost/docs

PGAdmin, PostgreSQL web administration: http://localhost:5050