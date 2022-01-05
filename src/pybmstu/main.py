import click
from pybmstu import tex

@click.group("cli")
def cli():
    pass

@cli.command("tex")
@click.argument("type")
def cmd_tex(type):
    """Generates texdoc from template.

    TYPE can be one of "report", "lab", "paper" or "rpz".
    """
    
    if type in ("report", "lab"):
        tex.gen_report()
        click.echo("report generated")
    elif type in ("paper", "rpz"):
        tex.gen_paper()
        click.echo("paper generated")
    else:
        raise click.BadParameter(f"'{type}' is not valid texdoc type")

if __name__ == "__main__":
    cli()
