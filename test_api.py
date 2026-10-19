
import requests_unixsocket

socket_url = (
    "http+unix://%2FUsers%2Fnicolasgrosso"
    "%2F.colima%2Fdefault%2Fincus.sock"
)

session = requests_unixsocket.Session()

response = session.get(
    f"{socket_url}/1.0/instances?recursion=2"
)
response.raise_for_status()

data = response.json()

if data["status"] != "Success":
    raise RuntimeError(data["error"])

for instance in data["metadata"]:
    print(f"Name: {instance['name']}")
    print(f"Status: {instance['status']}")
    print(f"Type: {instance['type']}")
    print(f"Architecture: {instance['architecture']}")
    print(f"Project: {instance['project']}")
    print()
