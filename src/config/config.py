import os
from dotenv import load_dotenv

load_dotenv() 

config = {
    'db_url': os.getenv('DB_URL') or '',
    'port': os.getenv('DB_PORT') or '',
    'user': os.getenv('DB_USER') or '',
    'password': os.getenv('DB_PASSWORD') or '',
    'host': os.getenv('DB_HOST') or '',
    'db_name': os.getenv('DB_NAME') or ''
}
