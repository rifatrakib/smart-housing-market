# Smart Housing Market

This repository contains the source code for the course project of *Software Project Management (研一)* and *Software Requirement Engineering (研二)* completed in a joint effort of [Md Abdur Rakib](https://www.linkedin.com/in/md-abdur-rakib-1508/), [Md Talat Mahmud Tomal](https://www.linkedin.com/in/talatmcc), and [S.B. Babu](https://www.linkedin.com/in/s-b-babu-09071332b/). The project mainly focuses on corporate practices followed within a team of engineers at a real workplace via a framework decided by the organization, but as this project is done in order to learn, the process has been simulated at a lower scale.

## Related Project

You can find the projects we defined and documented for this application in the `Projects` tab of this repository. Please find the *open* projects here: [https://github.com/rifatrakib/smart-housing-market/projects?query=is%3Aopen](https://github.com/rifatrakib/smart-housing-market/projects?query=is%3Aopen) and the *closed* projects here: [https://github.com/rifatrakib/smart-housing-market/projects?query=is%3Aclosed](https://github.com/rifatrakib/smart-housing-market/projects?query=is%3Aclosed). By the time we complete this application, all these projects should have *closed* status.

### Components

This application has 3 major components or sub-applications:

1. A client app built using [Sveltekit](https://kit.svelte.dev/) with server-side-rendering (*SSR*) capabilities.
2. A REST API built using [FastAPI](https://fastapi.tiangolo.com/).
3. A collection of pipelines which demonstrates end-to-end machine learning pipelines.

### Deploy the application

To make things simpler, we have included a simple CLI application in this repository which takes care of all necessary steps to deploy or terminate the application using a single command instead of having to go through many steps. To use the CLI, all you need is the following:

* Docker (Linux), and Docker Desktop (Windows/MacOS)
* Python (This is only to be able to use the CLI).

That's it! You can skip installing python if you are willing to manually handle some steps to run the application on docker, we will also detail those steps below.

##### Simpler approach

Once you have Docker (and/or Docker Desktop) and Python installed, run the following commands to deploy the application on docker:

**Please create a virtual environment on your own. Find how to do it for your OS. This is highly recommended, but not mandatory.**

```
pip install poetry
poetry install
```

This will allow you to use the CLI that comes with this repository. Next, you have two options:

```
python manage.py deploy --mode development
```

which will run the application in development mode. Or,

```
python manage.py deploy
```

this will show you the available modes and allow you to type your input.

**THAT'S IT!** This will deploy the application on docker and you can access the client application using `http://127.0.0.1:5173` and the server side application will be available on the host `http://127.0.0.1:8000`.

##### Manual approach

To manually deploy the applications, please follow the `README.md` files inside the `/client` and `/api` directories.
