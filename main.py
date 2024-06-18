import click
from src.services.user_services import UserService


@click.command()
@click.option('--name', help='Your name')
def hello( name ):
    click.echo(message=f"Hello world {name}", color=True)

@click.command()
def find_users():
    users = UserService()
    click.echo(users.find_users())

if __name__ == '__main__':
    pass