"""Check network."""


import asyncio
import subprocess

from halo import Halo

from netcheck.datatypes import ip_status

ip_list = ["1.1.1.1", "9.9.9.9", "10.0.0.10"]


async def async_ping(ip):
    """Ping ip address.

    Args:
        ip: ip address

    Returns:
        namedtupe(ip, status)
    """
    reply = await asyncio.create_subprocess_shell(
        f"ping -c 3 -n {ip}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await reply.communicate()

    status = "reachable" if reply.returncode == 0 else "unreachable"
    return ip_status(ip, status)


async def async_ping_ip_list(ip_list):
    """Run async ping.

    Args:
        ip_list: lis of addresses

    Returns:
        list of results
    """
    coroutines = [async_ping(ip) for ip in ip_list]
    result = await asyncio.gather(*coroutines)
    return result


def ping(ip):
    """Ping IP.

    Args:
        ip: ip address

    Returns:
        bool value
    """
    reply = subprocess.run(  # noqa: S607
        ["ping", "-c", "3", ip],
        capture_output=True,
    )  # noqa: S607, WPS110
    status = "reachable" if reply.returncode == 0 else "unreachable"
    return ip_status(ip, status)


def find_gw():
    """Find GW."""
    pass  # noqa: WPS420


def network_check():
    """Check network.

    Returns:
        result
    """
    with Halo(text="Loading", spinner="dots"):
        return [ping(ip) for ip in ip_list]


def async_network_check():
    with Halo(text="Loading", spinner="dots"):
        return asyncio.run(async_ping_ip_list(ip_list))
