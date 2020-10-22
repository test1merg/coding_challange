import requests
import json
import mysql.connector

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
        elif dbTable == "counterparty":
            query2 = "INSERT INTO " + dbTable + " (" + idValue + ", " + dbValue + ", 'A', ) VALUES(%s, %s)" #sql injection
        
        data = (variable_id, variable_name)
        cur.execute(query2, data)

        #print(str(variable_id) + " " + variable_name)

    conn.commit()


def addDeal(data):

    instrument_name = data["instrumentName"]
    counterparty_name = data["cpty"]
    price = data["price"]
    type_bs = data["type"]
    quantity = data["quantity"]
    time = data["time"]

    cur.execute("SELECT deal_id FROM deal WHERE deal_id = (SELECT MAX(deal_id) FROM deal)")
    deal_id = cur.fetchone()
    
    deal_id = deal_id[0] + 1

    print("deal_id " + str(deal_id))

    instrument_query = "SELECT instrument_id FROM instrument WHERE instrument_name = %s"
    cur.execute(instrument_query, (instrument_name,))
    instrument_id = cur.fetchone()[0]

    print("instrument_id " + str(instrument_id))

    counterparty_query = "SELECT counterparty_id FROM counterparty WHERE counterparty_name = %s"
    cur.execute(counterparty_query, (counterparty_name,))
    counterparty_id = cur.fetchone()[0]

    print("ctpy_id" + str(counterparty_id))

    deal_query = "INSERT INTO deal(deal_id, deal_time, deal_counterparty_id, deal_instrument_id, \
    deal_type, deal_amount, deal_quantity) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
    deal_data = (deal_id, time, counterparty_id, instrument_id, type_bs, price, quantity)
    cur.execute(deal_query, deal_data)

    conn.commit()


def verifyLogin(json):
    username = json["username"]
    pwd = json["password"]

    login_query = "SELECT user_id, user_pwd FROM users WHERE user_id = %s"
    cur.execute(login_query, (username,))
    result = cur.fetchone()

    if result == None:
        return False
    else:
        if result[1] == pwd:
            return True
        else:
            return False


# Connecting to the database
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "ppp",
    database = "db_grad_cs_1917",
    port = 3306
)

# Fetching data
url = "http://127.0.0.1:8080/streamTest"
response = requests.get(url, stream=True)

# test execute to assure that access is given
cur = conn.cursor() # in order to execute querys

#cur.execute("DELETE FROM instrument;",)

print(verifyLogin({"username" : "alison1", "password" : "h"}))
print(verifyLogin({"username" : "alison", "password" : "h"}))
print(verifyLogin({"username" : "alison", "password" : "gradprog2016@07"}))

'''
for line in response.iter_lines():
    if line:

        data = json.loads(line)
        print(data)
        #addEntry(data, "instrumentName", "instrument_name", "instrument_id", "instrument", 1001)
        addDeal(data)
'''

for x in cur:
    print(x)

#close connection
conn.close()