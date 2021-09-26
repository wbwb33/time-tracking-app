FROM node:12-alpine

ENV NUXT_VERSION=2.15.7

WORKDIR /app

COPY package.json package-lock.json /app/
RUN npm install

COPY . /app
RUN npm run generate
RUN rm -rf node_modules
RUN rm package.json package-lock.json
RUN yarn add "nuxt-start@${NUXT_VERSION}"
RUN yarn cache clean

ENTRYPOINT ["npx", "nuxt-start"]
EXPOSE 80