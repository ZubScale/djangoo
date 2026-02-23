import pymysql
import os

pymysql.install_as_MySQLdb()

# Monkey patch version to satisfy Django
import MySQLdb
if not hasattr(MySQLdb, 'version_info'):
    MySQLdb.version_info = (2, 2, 8, 'final', 0)
else:
    # Make sure it looks new enough
    MySQLdb.version_info = (2, 2, 8, 'final', 0)

# Check and create database if not exists
try:
    host = os.environ.get('DB_HOST', 'localhost')
    port = int(os.environ.get('DB_PORT', '3306'))
    user = os.environ.get('DB_USER', 'root')
    password = os.environ.get('DB_PASSWORD', '')
    dbname = os.environ.get('DB_NAME', 'djangoo')

    # Connect to MySQL server (without selecting a DB)
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    cursor = connection.cursor()
    # Create the database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    cursor.close()
    connection.close()
except Exception:
    # Fail silently or log if needed, but don't crash startup if DB is unreachable
    # (Django will complain later if it needs it)
    pass
