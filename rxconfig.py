import os

from reflex import Config
from dotenv import load_dotenv

load_dotenv()

port: int = os.getenv("DBPORT", 3306)
user: str = os.getenv("DBUSER")
host: str = os.getenv("DBHOST")
password: str = os.getenv("DBPASS")
database: str = os.getenv("DBNAME")

config = Config(
    app_name="grupal",
    db_url=f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}",
)
