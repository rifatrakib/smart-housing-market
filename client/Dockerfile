FROM node:current-slim

WORKDIR /client

COPY package*.json ./
RUN npm ci

COPY . .

RUN npm run build
EXPOSE 5173

CMD npm run dev
