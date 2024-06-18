from mysql.connector import connect, Error
from src import config


try:
    connection = connect( 
        host= config['host'],
        user= config['user'],
        password= config['password'],
        port= config['port'],
        database= config['db_name']
    )
    if connection.is_connected():
        pass
except  Error as err:
    print(f"Error {err}")       