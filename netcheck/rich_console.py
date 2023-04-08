"""Rich console."""

from rich.console import Console
from rich.table import Table

console = Console()


def print_table(items):
    """Print table with itwms.

    Args:
        items: list of namedtuples
    """
    table = Table(title="NetCheck")

    table.add_column("IP address / Domain name", justify="center")
    table.add_column("Description", justify="center")
    table.add_column("Status", justify="center")

    for item in items:
        status_color = "green" if item.status == "reachable" else "red"
        table.add_row(
            item.ip,
            item.description,
            f"[{status_color}]{item.status}[/{status_color}]",
        )

    console.print(table)
