#!/usr/bin/env python3
import json, socket, sys

HOSTS = {"cli": {"dns": "cli.au.team", "fallback": "20.20.20.151"}}

def resolve(h):
    try:
        return socket.gethostbyname(h["dns"])
    except OSError:
        return h["fallback"]

inventory = {
    "clients": {"hosts": list(HOSTS)},
    "_meta": {"hostvars": {n: {"ansible_host": resolve(h)} for n, h in HOSTS.items()}},
}

if len(sys.argv) > 1 and sys.argv[1] == "--host":
    print(json.dumps(inventory["_meta"]["hostvars"].get(sys.argv[2], {})))
else:
    print(json.dumps(inventory, indent=2))
