"""Check network."""


import click

from netcheck.network_check import async_network_check, network_check


@click.command()
@click.option("--async_ping", default=False)
def main(async_ping):
    """Run main func.

    Args:
        async_ping: if True run async ping
    """
    if async_ping:
        print(async_network_check())
    else:
        print(network_check())


if __name__ == "__main__":
    main()
