import mysql.connector

# Connecting to the database
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "ppp",
    database = "db_grad_cs_1917",
    port = 3306
)

# test execute to assure that access is given
cur = conn.cursor() # in order to execute querys

cur.execute("SHOW DATABASES")

for x in cur:
    print(x)

#close connection
conn.close()