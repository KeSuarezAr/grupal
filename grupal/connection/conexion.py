from sqlmodel import create_engine
from sqlalchemy import Engine


def create_database_engine(
    user: str = "root",
    password: str = "",
    host: str = "localhost",
    port: int = 3306,
    database: str = "grupal_interfaces",
) -> Engine:
    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    return create_engine(url)
