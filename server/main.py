import flask
from flask import request
import util

app = flask.Flask (__name__)


@app.route ('/get_airline_names', methods=['GET'])
def get_airline_name():
    response = flask.jsonify ({
        'airlines': util.get_airline_name ()
    })
    response.headers.add ('Access-Control-Allow-Origin', '*')

    return response


@app.route ('/get_origin_names', methods=['GET'])
def get_origin_name():
    response = flask.jsonify ({
        'origin': util.get_origin_name ()
    })
    response.headers.add ('Access-Control-Allow-Origin', '*')

    return response


@app.route ('/get_destination_names', methods=['GET'])
def get_destination_name():
    response = flask.jsonify ({
        'destination': util.get_destination_name ()
    })
    response.headers.add ('Access-Control-Allow-Origin', '*')

    return response


@app.route ('/predict_delay', methods=['GET', 'POST'])
def predict_delay():
    AIRLINE = flask.request.form['AIRLINE']
    ORIGIN_AIRPORT = flask.request.form['ORIGIN_AIRPORT']
    DESTINATION_AIRPORT = flask.request.form['DESTINATION_AIRPORT']
    MONTH = int (flask.request.form['MONTH'])
    DAY = int (flask.request.form['DAY'])
    DAY_OF_WEEK = int (flask.request.form['DAY_OF_WEEK'])
    SCHEDULED_DEPARTURE = int (flask.request.form['SCHEDULED_DEPARTURE'])
    DEPARTURE_TIME = int (flask.request.form['DEPARTURE_TIME'])
    DEPARTURE_DELAY = float (flask.request.form['DEPARTURE_DELAY'])
    TAXI_OUT = float (flask.request.form['TAXI_OUT'])
    SCHEDULED_ARRIVAL = int (flask.request.form['SCHEDULED_ARRIVAL'])

    response = flask.jsonify (dict (
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
