"""Check network."""


import click

from netcheck.network_check import network_check
from netcheck.rich_console import print_table


@click.command()
def main():
    """Run main func."""
    res = network_check()
    print_table(res)


if __name__ == "__main__":
    main()
