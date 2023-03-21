import pandas as pd
import json 
from decouple import config
import requests

from game_plans.minecraft_config import mc_config

# Global req url and headers
URL = config("PTERYDACTYL_PANEL_URL")

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'Application/vnd.pterodactyl.v1+json',
    'Authorization': f'Bearer {config("PTERYDACTYL_APPLICATION_TOKEN")}'
}


def get_user_id(email): # get the user id from panel, use email as filter

    # add filter to url
    url = f"{URL}/api/application/users?filter[email]={email}"

    response = requests.request("GET", url, headers=HEADERS)

    #print(response.text)

    # load data into json and extract id
    response = json.loads(response.text)
    id = response["data"][0]["attributes"]["id"]

    return id

def simple_allocation():
    url = f'{URL}/api/application/nodes'

    # Find nodes with empty allocation slots
    for node_id in range(1, json.loads(requests.request("GET", url, headers=HEADERS).text)["meta"]["pagination"]["total"]+1):
        resonse = requests.request("GET", f'{url}/{node_id}/allocations', headers=HEADERS)
        for allocation in json.loads(resonse.text)["data"]:
            if allocation["attributes"]["assigned"]:
                continue
            return allocation["attributes"]["id"]
    raise Exeption("NO FREE ALLOCATIONS AVAILABLE")



def create_server(request):
    """
    CONFIG:
    {
        "name": "",
        "user": 0,
        "egg": 1,
        "docker_image": "quay.io/pterodactyl/core:java",
        "startup": "java -Xms128M -Xmx128M -jar server.jar",
        "environment": {
            "BUNGEE_VERSION": "latest",
            "SERVER_JARFILE": "server.jar"
        },
        "limits": {
            "memory": 0,
            "swap": 0,
            "disk": 0,
            "io": 0,
            "cpu": 0
        },
        "feature_limits": {
            "databases": 0,
            "backups": 0
        },
        "allocation": {
            "default": 17
        }
    }

    request must include:
    {
        "email":,
        "plan":,
        "game":,
    }

    """

    user_id = get_user_id(request.get_json()["email"])

    allocation_id = simple_allocation()

    #import correct config
    game_config = {}
    match request.get_json()["game"]:
        case "minecraft":
            game_config = mc_config(request.get_json()["plan"])

    # add server name and user id
    game_config["name"] = f"{request.get_json()['email'].split('@')[0]} - {request.get_json()['plan']}"
    game_config["user"] = int(user_id)
    game_config["allocation"]["default"] = int(allocation_id)

    url = f"{URL}/api/application/servers"

    #print(json.dumps(game_config))

    response = requests.request("POST", url, headers=HEADERS, data=json.dumps(game_config))

    print(response.text)

    return

