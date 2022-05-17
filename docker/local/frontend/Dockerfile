ARG NODE_VERSION=16

FROM node:${NODE_VERSION} as node

FROM node as client-local-build

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./frontend/package*.json .

#COPY ./frontend ${APP_HOME}

RUN npm install


CMD ["npm","start"]
