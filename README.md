# Actividad 3 - Automatización de Base de Datos

## Descripción

Proyecto en Python que utiliza SQLAlchemy y Faker para crear y poblar una base de datos MySQL con 100.000 registros.

---

## Tecnologías usadas

- Python
- MySQL
- SQLAlchemy
- Faker
- PyMySQL
- python-dotenv

---

## Instalación

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Configuración

Crear archivo `.env`

```env
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=actividad3
```

---

## Crear Base de Datos

En MySQL ejecutar:

```sql
CREATE DATABASE actividad3;
```

---

## Ejecución

```bash
python main.py
```

---

## Exportar a CSV

Después de ejecutar el script, puedes exportar la tabla `personas_yudy` a un archivo CSV:

```bash
python export_personas_csv.py
```

El archivo resultante se guardará como `personas_yudy.csv`.

---

## Resultado esperado

La tabla `personas_yudy` contendrá 100.000 registros generados automáticamente.
