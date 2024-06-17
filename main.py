import click

@click.command()
def hello():
    click.echo(message="Hello world", color=True)

if __name__ == '__main__':
    hello()    