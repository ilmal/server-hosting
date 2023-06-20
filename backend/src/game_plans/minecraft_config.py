import json

BASIC = {
    "price": 10,
    "cpu": 200,
    "memory": 2000,
    "disk": 5000,
    "backups": 3
}

NORMAL = {
    "price": 15,
    "cpu": 300,
    "memory": 4000,
    "disk": 10000,
    "backups": 10
} 

PREMIUM = {
    "price": 20,
    "cpu": 400,
    "memory": 8000,
    "disk": 15000,
    "backups": 10
}

template = {
    "name": "",
    "user": 0,
    "egg": 3,
    "docker_image": "ghcr.io/pterodactyl/yolks:java_17",
    "startup": "java -Xms128M -XX:MaxRAMPercentage=95.0 -Dterminal.jline=false -Dterminal.ansi=true -jar {{SERVER_JARFILE}}",
    "environment": {
        "SERVER_JARFILE": "server.jar",
        "BUILD_NUMBER": "latest",
        "MINECRAFT_VERSION": "latest"
    },
    "limits": {
        "memory": 0,
        "swap": 0,
        "disk": 0,
        "io": 500,
        "cpu": 0
    },
    "feature_limits": {
        "databases": 0,
        "backups": 0
    },
    "allocation": {
        "default": 0
    }
}

def build_config(plan_values):
    template["limits"]["memory"] = plan_values["memory"]
    template["limits"]["disk"] = plan_values["disk"]
    template["limits"]["cpu"] = plan_values["cpu"]
    template["feature_limits"]["backups"] = plan_values["backups"]
    return template

def mc_config(plan):
    match plan:
        case "basic":
            config = build_config(BASIC)
        case "normal":
            config = build_config(NORMAL)
        case "premium":
            config = build_config(PREMIUM)
    return config

def get_plan_data(plan):
    match plan:
        case "basic": return BASIC
        case "normal": return NORMAL
        case "premium": return PREMIUM
    Exception("CUSTOM ERR, plan inserted in get_plan_data() is not correct!")
