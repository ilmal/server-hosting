import requests
import json
from decouple import config


def create_user(request):
    """
    json format must be: 
    {
        "email": "",
        "username": "",
        "first_name": "",
        "last_name": ""
    }
    """
    url = f"{config('PTERYDACTYL_PANEL_URL')}/api/application/users"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'Application/vnd.pterodactyl.v1+json',
        'Authorization': f'Bearer {config("PTERYDACTYL_APPLICATION_TOKEN")}'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(request.get_json()))

    print(response.text)

    return