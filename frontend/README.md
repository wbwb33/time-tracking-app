# Time Tracking Frontend

## Frontend Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Node](https://nodejs.org/en/download/).

## Frontend local development

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:8888
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

## Local deployment
Start with Docker Compose (will take some time to up), it will run on port 8888:

```bash
docker-compose up
```


### Frontend tests
```bash
$ npm install
$ npm run test
```