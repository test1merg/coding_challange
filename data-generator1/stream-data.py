import requests
import json
import mysql.connector

'''
instrument_name = data["instrumentName"]
    #print(instrument_name)

    query1 = "SELECT instrument_name FROM instrument WHERE instrument_name = %s"
    cur.execute(query1, (instrument_name,))
    instrument_result = cur.fetchone()

    print(instrument_result)
    

    if instrument_result == None:
    
        cur.execute("SELECT * FROM instrument WHERE instrument_id = (SELECT MAX(instrument_id) FROM instrument)")
        instrument_id = cur.fetchone()
    
        if instrument_id == None:
            instrument_id = 1001
        else:
            instrument_id = instrument_id[0] + 1

        

        query2 = "INSERT INTO instrument (instrument_id, instrument_name) VALUES(%s, %s)" #sql injection
        data = (instrument_id, instrument_name)
        cur.execute(query2, data)

        #print(str(instrument_id) + " " + instrument_name)

    conn.commit()
'''

# data = original json line, jsonValue = key name, dbValue = column name, idValue = id primary key, 
# dbTable = table from db, idCounter = beginning value for id

# data, instrumentName, instrument_name, instrument_id, instrument, 1001
# data, cpty (counterparty name), counterparty_name, counterparty_id, counterparty, 701
def addEntry(data, jsonValue, dbValue, idValue, dbTable, idCounter):

    variable_name = data[jsonValue]

    query1 = "SELECT " + dbValue + " FROM " + dbTable + " WHERE " + dbValue + " = %s"
    cur.execute(query1, (variable_name,))
    result = cur.fetchone()

    print(result)
    
    if result == None:
    
        cur.execute("SELECT * FROM " + dbTable + " WHERE " + idValue + " = (SELECT MAX(" + idValue + ") FROM " + dbTable + ")")
        variable_id = cur.fetchone()
    
        if variable_id == None:
            variable_id = idCounter
        else:
            variable_id = variable_id[0] + 1

        if dbTable == "instrument":
            query2 = "INSERT INTO " + dbTable + " (" + idValue + ", " + dbValue + ") VALUES(%s, %s)" #sql injection
        else if dbTable == "counterparty":
            query2 = "INSERT INTO " + dbTable + " (" + idValue + ", " + dbValue + ", 'A', ) VALUES(%s, %s)" #sql injection
        
        data = (variable_id, variable_name)
        cur.execute(query2, data)

        #print(str(variable_id) + " " + variable_name)

    conn.commit()




# Connecting to the database
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "ppp",
    database = "db_grad_cs_1917_no_deal_data",
    port = 3306
)

# Fetching data
url = "http://127.0.0.1:8080/streamTest"
response = requests.get(url, stream=True)

# test execute to assure that access is given
cur = conn.cursor() # in order to execute querys

#cur.execute("DELETE FROM instrument;",)

for line in response.iter_lines():
    if line:

        data = json.loads(line)
        addEntry(data, "instrumentName", "instrument_name", "instrument_id", "instrument", 1001)
        

#conn.commit()

for x in cur:
    print(x)

#close connection
conn.close()