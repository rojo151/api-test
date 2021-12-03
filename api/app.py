import os
from flask import Flask, jsonify, request,g
import pymongo
import time
from datetime import datetime

app = Flask(__name__)

#-- Writer on MongoDB placed in container --#
def write_to_db(data):
    client = pymongo.MongoClient(
        "mongodb://"+os.environ['ENV_USER']+":"+os.environ['ENV_PWD']+"@"+os.environ['ENV_HOST']+":27017/")    
    databaseRunning = client["testClient"]
    collectionSelected = databaseRunning["jsonCollection"]
    collectionSelected.insert_one(data)
 

#-- Intro page --#
@app.route('/')
def main():
    return ''

#-- JSON handler --#
@app.route('/partium/echoservice', methods=['POST']) 
def json_handler():
    decoded_response = request.json
    additionalData = {'requestTime': datetime.now(), 'unixTimeStamp': time.time()}
    decoded_response.update(additionalData)
    g.formatted_response = decoded_response   
    return jsonify(decoded_response)


#-- Database handler--#
@app.teardown_request
def database_handler(error=None):
    dataDB = g.get('formatted_response')
    write_to_db(dataDB)


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)