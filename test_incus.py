import json
import subprocess


import json
import subprocess

# Query the Incus API through the CLI
result = subprocess.run(
    ["incus", "query", "/1.0/instances/test"],
    capture_output=True,
    text=True,
    check=True,
)

# Convert the received JSON into a Python dictionary
instance = json.loads(result.stdout)

# Read some fields
print("Name:", instance["name"])
print("Status:", instance["status"])
print("Type:", instance["type"])
