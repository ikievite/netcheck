"""Sync Check."""

import subprocess

from netcheck.datatypes import ip_status


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


def sync_network_check(ip_list):
    """Check network.

    Args:
        ip_list: list of ip addresses

    Returns:
        result
    """
    return [ping(ip) for ip in ip_list]
