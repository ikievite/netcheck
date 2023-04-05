"""Check network."""


import click

from netcheck.network_check import network_check


@click.command()
def main():
    """Run main func."""
    network_check()


if __name__ == "__main__":
    main()
