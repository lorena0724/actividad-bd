from sqlalchemy import create_engine, text
from faker import Faker
from dotenv import load_dotenv
import os
import random
import sys

# cargar variables del .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Verificar variables de entorno
missing = [v for v in ("DB_USER","DB_PASSWORD","DB_HOST","DB_PORT","DB_NAME") if not os.getenv(v)]
if missing:
    print("Faltan variables de entorno:", ", ".join(missing))
    print("Crea un archivo .env con DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME o exporta las variables.")
    sys.exit(1)

# conexión MySQL
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# engine SQLAlchemy
engine = create_engine(DATABASE_URL)

# faker en español
faker = Faker("es_ES")


def crear_tabla():

    query = """
    CREATE TABLE IF NOT EXISTS personas_yudy (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        correo VARCHAR(100),
        ciudad VARCHAR(100),
        telefono VARCHAR(50),
        direccion VARCHAR(150),
        fecha_nacimiento DATE,
        empresa VARCHAR(100),
        salario FLOAT
    );
    """

    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()


def generar_datos(cantidad=100000):

    lista_personas = []

    for _ in range(cantidad):

        persona = {
            "nombre": faker.name(),
            "correo": faker.email(),
            "ciudad": faker.city(),
            "telefono": faker.phone_number(),
            "direccion": faker.address(),
            "fecha_nacimiento": faker.date_of_birth(
                minimum_age=18,
                maximum_age=80
            ),
            "empresa": faker.company(),
            "salario": round(
                random.uniform(1000000, 10000000), 2
            )
        }

        lista_personas.append(persona)

    return lista_personas


def insertar_datos(datos):

    query = text("""
        INSERT INTO personas_yudy
        (
            nombre,
            correo,
            ciudad,
            telefono,
            direccion,
            fecha_nacimiento,
            empresa,
            salario
        )
        VALUES
        (
            :nombre,
            :correo,
            :ciudad,
            :telefono,
            :direccion,
            :fecha_nacimiento,
            :empresa,
            :salario
        )
    """)

    with engine.connect() as conn:
        conn.execute(query, datos)
        conn.commit()


def main():

    print("Creando tabla...")
    crear_tabla()

    print("Generando registros...")
    datos = generar_datos()

    print("Insertando registros... (esto puede tardar mucho)")
    insertar_datos(datos)

    print("Proceso finalizado correctamente")


if __name__ == "__main__":
    main()
