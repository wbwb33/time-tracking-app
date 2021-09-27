FROM node:12-alpine as builder

WORKDIR /build

COPY package.json package-lock.json /build/
RUN npm install

COPY . /build
RUN npm run generate



FROM node:12-alpine as app

RUN npm install -g "http-server@13.0.2"

WORKDIR /app
COPY --from=builder /build/dist /app/public

ENTRYPOINT ["http-server", "-p", "80"]
EXPOSE 80