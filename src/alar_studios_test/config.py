import os
from pathlib import Path

from dotenv import load_dotenv

DOTENV_FILE = Path.cwd() / '.env'

if DOTENV_FILE.exists():
    load_dotenv(dotenv_path=Path.cwd() / '.env')
else:
    load_dotenv()

CODE_PATH = Path(__file__).parent
PROJECT_PATH = CODE_PATH.parent.parent

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_URL = f'{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
DB_URL = f'postgresql+psycopg2://{POSTGRES_URL}'

SESSION_DURATION = int(os.getenv('SESSION_DURATION'))
