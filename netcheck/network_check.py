"""Check network."""


import subprocess

ip_addresses = ["1.1.1.1", "9.9.9.9", "10.0.0.10"]


def ping_ip(ip):
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
    return reply.returncode == 0


def find_gw():
    """Find GW."""
    pass  # noqa: WPS420


def network_check():
    """Check network.

    Returns:
        result
    """
    request = []
    for ip in ip_addresses:
        if ping_ip(ip):
            request.append(f"IP address {ip} is available.")
        else:
            request.append(f"IP address {ip} is unreachable.")
    return "\n".join(request)
