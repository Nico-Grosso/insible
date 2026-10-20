
from incus_api import get_instances


instances = get_instances()

for instance in instances:
    print(f"Name: {instance['name']}")
    print(f"Status: {instance['status']}")
    print(f"Type: {instance['type']}")
    print()
