# Smart Housing Market - API

This directory contains the codes used for building the server side application for the smart housing market application. This is a REST API built using [FastAPI](https://fastapi.tiangolo.com/).

### Requirements

Here's a list of things you will need to run this server side application:

* Python
* MongoDB
* Redis

### Deployment

Make sure to have a `.env` file having necessary configuration variables defined properly. **Mind that, this approach will require you to modify this file if you want to run the application in a different mode, and you don't have an automated way to create this file for you with the correct configuration values for different modes.**. Once you have everything installed, you can run the following commands to have the server side application start listening on port 8000 from inside the `/api` directory:

**Please create a virtual environment on your own. Find how to do it for your OS. This is highly recommended, but not mandatory**.
**NOTE THAT, THIS WILL NEED A SEPARATE VIRTUAL ENVIRONMENT THAN THE ONE AT THE ROOT DIRECTORY**

Run the following command to run the application directly on your machine:

```
pip install poetry
poetry install
uvicorn src.main:app --reload
```

or build and run on docker:

```
docker build -t smart-housing-market-api .
docker run -p 8000:8000 smart-housing-market-api
```
