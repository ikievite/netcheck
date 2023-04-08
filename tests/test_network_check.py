"""Test netcheck."""


from ipaddress import IPv4Address

from netcheck.network_check import find_gw


def test_find_gw():
    gw = find_gw()
    assert isinstance(gw, list)
    if len(gw) > 1:
        for intf_ip in gw:
            for ip in intf_ip.values():
                assert IPv4Address(ip)
