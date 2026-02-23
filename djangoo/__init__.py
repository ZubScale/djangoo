import pymysql

pymysql.install_as_MySQLdb()

# Monkey patch version to satisfy Django
import MySQLdb
if not hasattr(MySQLdb, 'version_info'):
    MySQLdb.version_info = (2, 2, 8, 'final', 0)
else:
    # Make sure it looks new enough
    MySQLdb.version_info = (2, 2, 8, 'final', 0)
