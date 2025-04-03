from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# load the .env file variables
load_dotenv()


def db_connect():
    import os
    engine = create_engine(os.getenv('DATABASE_URL'))
    engine.connect()
    return engine

def separar_imagenes(ruta_carpeta):
    archivos = os.listdir(ruta_carpeta)
    for archivo in archivos:
        if archivo.startswith('dog'):
            destino = os.path.join(ruta_carpeta, 'dog')
        elif archivo.startswith('cat'):
            destino = os.path.join(ruta_carpeta, 'cat')
        else:
            pass
        shutil.move(os.path.join(ruta_carpeta, archivo), destino)
