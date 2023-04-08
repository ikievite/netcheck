"""Check network."""


import asyncio
import json
import os
import subprocess

from dotenv import load_dotenv

from netcheck.datatypes import ip_status
from netcheck.rich_console import console

load_dotenv()

IP_DICT = json.loads(os.getenv("IP_DICT", "{}"))

show_show_default_route = "ip --json route show default".split()
ping_ip_command = "ping -i 0,2 -c 3 -n -W 1 {ip}"


async def async_ping(ip, desc):
    """Ping ip address.

    Args:
        ip: ip address
        desc: description

    Returns:
        namedtupe(ip, description, status)
    """
    reply = await asyncio.create_subprocess_shell(
        ping_ip_command.format(ip=ip),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await reply.communicate()

    status = "reachable" if reply.returncode == 0 else "unreachable"
    return ip_status(ip, desc, status)


async def async_ping_ip_dict(ip_dict):
    """Run async ping.

    Args:
        ip_dict: dict of description: addresses

    Returns:
        list of results
    """
    coroutines = [async_ping(ip, desc) for desc, ip in ip_dict.items()]
    res = await asyncio.gather(*coroutines)
    return res


def find_gw():
    """Find GW.

    Returns:
        list of dict dev: desc
    """
    reply = subprocess.run(
        show_show_default_route,
        capture_output=True,
        encoding="utf-8",
    )
    routes = json.loads(reply.stdout)
    return [{route.get("dev"): route.get("gateway")} for route in routes]


def async_network_check(ip_dict):
    """Run asyncio.

    Args:
        ip_dict: dict with ip: description

    Returns:
        list of namedtuples
    """
    return asyncio.run(async_ping_ip_dict(ip_dict))


def network_check():
    """Check network.

    Returns:
        list of namedtuples
    """
    with console.status("Checking", spinner="bouncingBall"):
        gateways = find_gw()
        for gw in gateways:
            IP_DICT.update(gw)
        res = async_network_check(IP_DICT)

    return res
