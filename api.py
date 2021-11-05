#!/usr/bin/env python

import json
import time
import requests
from flask import Flask
from flask import request
import syslog

app = Flask(__name__)

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/select/"

@app.route("/iata")
def iata():
    url = "https://iata-and-icao-codes.p.rapidapi.com/airlines"

    headers = {
        'x-rapidapi-host': "iata-and-icao-codes.p.rapidapi.com",
        'x-rapidapi-key': "8a0ee99658msh391f0be5aa5d17fp170073jsnc2213f30ccc8"
        }

    result = requests.request("GET", url, headers=headers)

    jsonobj = json.loads(result.text)

    result = "<TABLE border='1'>"
    for key in jsonobj:
        result += '<TR>'
        for k,v in key.items():
            result += "<TD>{}</TD><TD>{}</TD>".format(k,v)
        result += "</TR>"
    result += "</TABLE>"

    response = app.response_class(
        status=200,
        mimetype="text/html",
        response=result
    )

    return response

@app.route("/sky")
def sky():
    
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/referral/v1.0/NL/EUR/en-gb/AMS-SKY/BCN-SKY/2021-10-30/2021-10-31"

    querystring = {"shortapikey":"ra66933236979928","apiKey":"{shortapikey}"}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "8a0ee99658msh391f0be5aa5d17fp170073jsnc2213f30ccc8"
        }

    result = requests.request("GET", url, headers=headers, params=querystring)

    response = app.response_class(
        status=200,
        mimetype="application/json",
        response=result
    )

    return response



if __name__ == '__main__':
  syslog.syslog('Processing started')
  syslog.syslog(syslog.LOG_ERR, 'Processing started')
  app.run(host="0.0.0.0")

