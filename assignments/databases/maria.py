# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="mdmfvz",
        password="my2BOYZ!",
        host="cs-class-db.srv.mst.edu",
        port=3306,
        database="mdmfvz"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute('INSERT INTO Books (Book_ID, Title, Release_Date, Location) VALUES (30577519075, "The Waste Land, Prufrock and Other Poems (Dover Thrift Editions)", NULL, "???");')

