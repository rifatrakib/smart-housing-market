import json
import subprocess
from enum import Enum

from typer import Option, Typer

app = Typer()


class Modes(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    STAGING = "staging"


def prepare_docker_compose_file(mode: str):
    try:
        with open(f"compose-templates/{mode}.yaml") as file:
            config = file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Docker compose template not found for the specified mode")

    with open("docker-compose.yaml", "w") as file:
        file.write(config)


def prepare_env_file(mode: str):
    try:
        with open(f"api/secrets/{mode}.json") as file:
            secrets = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Secrets file not found for the specified mode")

    with open("api/.env", "w") as file:
        file.write("\n".join([f"{key}={value}" for key, value in secrets.items()]))


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
        prepare_docker_compose_file(mode.value)
        prepare_env_file(mode.value)
    except FileNotFoundError as e:
        print(e.args[0])
        return

    subprocess.run("docker compose up --build -d", shell=True)


@app.command(name="terminate")
def terminate_applications():
    print("Terminating")
    subprocess.run("docker compose down", shell=True)
    subprocess.run('docker image prune --force --filter "dangling=true"', shell=True)


if __name__ == "__main__":
    app()
