# syntax=docker/dockerfile:1

FROM node:24-alpine AS builder

WORKDIR /frontend

RUN --mount=src=package.json,target=package.json \
    --mount=src=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci

COPY . .
RUN --mount=type=cache,target=/root/.npm \
    npm run build


FROM nginx:alpine AS release

WORKDIR /fe
RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /frontend/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]


