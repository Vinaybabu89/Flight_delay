from flask import Flask, jsonify
from flask import request
import util

app = Flask (__name__)


@app.route ('/get_airline_names', methods=['GET'])
def get_airline_name():
    response = jsonify ({
        'airlines': util.get_airline_name ()
    })
    response.headers.add ('Access-Control-Allow-Origin', '*')

    return response


@app.route ('/get_origin_names', methods=['GET'])
def get_origin_name():
    response = jsonify ({
        'origin': util.get_origin_name ()
    })
    response.headers.add ('Access-Control-Allow-Origin', '*')

    return response


@app.route ('/get_destination_names', methods=['GET'])
def get_destination_name():
    response = jsonify ({
        'destination': util.get_destination_name ()
    })
    response.headers.add ('Access-Control-Allow-Origin', '*')

    return response


@app.route ('/predict_delay', methods=['GET', 'POST'])
def predict_delay():
    AIRLINE = request.form['AIRLINE']
    ORIGIN_AIRPORT = request.form['ORIGIN_AIRPORT']
    DESTINATION_AIRPORT = request.form['DESTINATION_AIRPORT']
    MONTH = int (request.form['MONTH'])
    DAY = int (request.form['DAY'])
    DAY_OF_WEEK = int (request.form['DAY_OF_WEEK'])
    SCHEDULED_DEPARTURE = int (request.form['SCHEDULED_DEPARTURE'])
    DEPARTURE_TIME = int (request.form['DEPARTURE_TIME'])
    DEPARTURE_DELAY = float (request.form['DEPARTURE_DELAY'])
    TAXI_OUT = float (request.form['TAXI_OUT'])
    SCHEDULED_ARRIVAL = int (request.form['SCHEDULED_ARRIVAL'])

    response = jsonify (dict (
        estimated_delay=util.get_flight_delay (AIRLINE, ORIGIN_AIRPORT, DESTINATION_AIRPORT, MONTH, DAY, DAY_OF_WEEK,
                                               SCHEDULED_DEPARTURE, DEPARTURE_TIME,
                                               DEPARTURE_DELAY, TAXI_OUT, SCHEDULED_ARRIVAL
                                               )))
    response.headers.add ('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print ("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts ()
    app.run (debug=True)
