from flask import Flask, Response, request
from flask_cors import CORS
import webServiceStream
from RandomDealData import *
import UserValidationDAO
import streamData

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return webServiceStream.index()

@app.route('/testservice')
def testservice():
    return webServiceStream.testservice()

@app.route('/streamTest')
def stream():
    return webServiceStream.stream()

@app.route('/streamTest/sse')
def sse_stream():
     return webServiceStream.sse_stream()

@app.route('/validateLoginCreds', methods=["POST"])
def validate_creds():
    if request.method == "POST":
        data = request.get_json()["data"]
        print("true from data-gen : {}".format(data))
        result = UserValidationDAO.loginValidationCheck(data["email"], data["password"])
        print("result from data_gen {}".format(result))
        if result == 1:
            return "true"
        elif result == 0:
            return "false"
        else:
            return "error"

@app.route('/getHistoricData/<name>/<limit>', methods=["GET"])
def fetch_historic_data(name, limit):
    print("hi")
    result = streamData.getHistoricData(name, int(limit))
    #print("result is {} with type {}".format(result, type(result)))
    return result

# @app.route('/getHistoricData/<counterparty_name>/<limit>', methods=["GET"])
# def fetch_historic_data(counterparty_name, limit):
#     url = "http://127.0.0.1:8080/getHistoricData/{}/{}".format(counterparty_name, limit)
#     result = stream-data.getHistoricData(counterparty_name, limit)
#     return result

def bootapp():
    #global rdd 
    #rdd = RandomDealData()
    #webServiceStream.bootServices()
    app.run(debug=True, port=8080, threaded=True, host=('0.0.0.0'))


if __name__ == "__main__":
      bootapp()
