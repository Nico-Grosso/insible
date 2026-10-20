
import requests_unixsocket
from utils import *


def get_instances():
    session = requests_unixsocket.Session()

    response = session.get(
        f"{SOCKET_URL}/1.0/instances?recursion=2"
    )
    response.raise_for_status()

    data = response.json()

    if data["status"] != "Success":
        raise RuntimeError(data["error"])

    return data["metadata"]
