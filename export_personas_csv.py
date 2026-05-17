import os
import csv
from dotenv import load_dotenv
import pymysql

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME")

output_path = "personas_yudy.csv"

conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    db=DB_NAME,
    port=DB_PORT,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.SSCursor,
)

try:
    with conn.cursor() as cur:
        cur.execute("SELECT id, nombre, correo, ciudad, telefono, direccion, fecha_nacimiento, empresa, salario FROM personas_yudy")
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # escribir cabeceras
            headers = [d[0] for d in cur.description]
            writer.writerow(headers)
            # escribir filas por streaming
            for row in cur:
                writer.writerow(row)
    print(f"Exportado CSV: {output_path}")
finally:
    conn.close()
