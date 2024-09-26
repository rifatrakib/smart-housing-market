import json
import subprocess
from enum import Enum

from typer import Option, Typer

app = Typer()


class Modes(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    STAGING = "staging"


@app.command(name="deploy")
def deploy_applications(
    mode: Modes = Option(
        prompt=True,
        show_choices=True,
        help="Mode of deployment (development/production/staging)",
    ),
):
    print(f"Deploying applications in {mode.value} mode ...")

    try:
        with open(f"api/secrets/{mode.value}.json") as file:
            secrets = json.load(file)
    except FileNotFoundError:
        print(f"Secrets file not found for {mode.value} mode")
        return

    with open("api/.env", "w") as file:
        file.write("\n".join([f"{key}={value}" for key, value in secrets.items()]))

    subprocess.run("docker compose up --build -d", shell=True)


@app.command(name="terminate")
def terminate_applications():
    print("Terminating")
    subprocess.run("docker compose down", shell=True)
    subprocess.run('docker image prune --force --filter "dangling=true"', shell=True)


if __name__ == "__main__":
    app()
