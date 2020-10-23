import requests
import json
import mysql.connector

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
    
    #Convert 20-Oct-2020 (10:13:24.895101)  to YYYY-MM-DDTHH:MM:SS.SSS
    months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06","Jul":"07",
    "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
    
    time_obj = time[7:11] + "-" + months[time[3:6]] + "-" + time[0:2] + "T" + time[13:25]

    deal_query = "INSERT INTO deal(deal_id, deal_time, deal_counterparty_id, deal_instrument_id, \
    deal_type, deal_amount, deal_quantity) VALUES(%s, %s, %s, %s, %s, %s, %s)" 
    deal_data = (deal_id, time_obj, counterparty_id, instrument_id, type_bs, price, quantity)
    cur.execute(deal_query, deal_data)

    conn.commit()


def getHistoricData(counterparty_name, limit):

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "ppp",
        database = "db_grad_cs_1917",
        port = 3306
    )

    cur = conn.cursor()

    counterparty_query = "SELECT counterparty_id FROM counterparty WHERE counterparty_name = %s;"
    cur.execute(counterparty_query, (counterparty_name,))
    counterparty_id = cur.fetchone()[0]

    deal_query = "SELECT * FROM deal WHERE deal_counterparty_id = %s ORDER BY deal_id DESC LIMIT %s;"

    #deal_query = "SELECT * FROM deal WHERE deal_counterparty_id = {} ORDER BY deal_id DESC LIMIT {}".format(counterparty_id,limit)
    #print("DEAL: " + deal_query)
    cur.execute(deal_query, (counterparty_id, limit))
    deal_results = cur.fetchall()

    deals = []

    for deal in deal_results:
        instrument_id = deal[3]
        instrument_query = "SELECT instrument_name FROM instrument WHERE instrument_id = %s;"
        cur.execute(instrument_query, (instrument_id,))
        instrument_name = cur.fetchone()[0]

        deal_dict = {"deal_id": deal[0],
                    "date": deal[1],
                    "counterparty_id": counterparty_id,
                    "counterparty_name": counterparty_name,
                    "instrument_id": instrument_id,
                    "instrument_name": instrument_name,
                    "deal_type": deal[4],
                    "deal_price": float(deal[5]),
                    "deal_quantity": deal[6]}

        deal_json = json.dumps(deal_dict)

        deals.append(deal_json)

    print(deals)
    conn.close()

    deals_json = json.dumps(deals)
    return deals_json


# Connecting to the database


# Fetching data
# url = "http://127.0.0.1:8080/streamTest"
# response = requests.get(url, stream=True)

# test execute to assure that access is given
#cur = conn.cursor() # in order to execute querys

#conn.commit()

#getHistoricData("Lewis", 5)
'''for line in response.iter_lines():
    if line:
        data = json.loads(line)
        print(data)
        addDeal(data)
'''

# for x in cur:
#     print(x)

#close connection
# conn.close()