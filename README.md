# Time Tracking App

## Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.
* [Node](https://nodejs.org/en/download/).

## Local deployment

Before going further, make sure to create `.env` files from `.env.example`. Take note at these keys, it's important:
```
BACKEND_CORS_ORIGINS=["http://localhost"]

BASE_URL=http://localhost:8888
```
You have to make sure these two keys is right, based on where you deploy. If you deploy at server, please adjust these keys to the IP of the server. `BASE_URL` is where the backend is located, `BACKEND_CORS_ORIGINS` is where the frontend is located.

Start with Docker Compose:

```bash
docker-compose up
```

Now you can open your browser and interact with these URLs:

Frontend (main app): http://localhost

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost/docs

PGAdmin, PostgreSQL web administration: http://localhost:5050

## App Overview

[![new-task.gif](https://s9.gifyu.com/images/new-task.gif)](https://gifyu.com/image/PBhQ)

## Unit Testing

Unit testing (BE/FE) is in their respective folders (Guide in README.md)