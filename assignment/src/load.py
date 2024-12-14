from typing import Dict
from pandas import DataFrame
from sqlalchemy.engine.base import Engine

def load(data_frames: Dict[str, DataFrame], database: Engine):
    """Carga los DataFrames en una base de datos SQLite utilizando SQLAlchemy.

    Args:
        data_frames (Dict[str, DataFrame]): Un diccionario donde las claves son los nombres 
        de las tablas y los valores son los DataFrames a cargar.
        database (Engine): El motor de SQLAlchemy conectado a la base de datos SQLite.

    Raises:
        Exception: Si ocurre un error durante la carga de los datos.
    """
    for key, value in data_frames.items():
        value.to_sql(key, database, if_exists='replace', index=False)
           
            








