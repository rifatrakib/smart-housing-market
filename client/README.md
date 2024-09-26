# Smart Housing Market - Client

This directory contains the codes used for building the client side application for the smart housing market application. This is a NodeJS application built using [sveltekit](https://kit.svelte.dev/).

### Requirements

Here's a list of things you will need to run this server side application:

* NodeJS
* NPM

### Deployment

Once you have everything installed, you can run the following commands to have the client side application start listening on port 5173 from inside the `/client` directory:

```
npm install
npm run dev
```

or build and run on docker:

```
docker build -t smart-housing-market-client .
docker run -p 5173:5173 smart-housing-market-client
```
