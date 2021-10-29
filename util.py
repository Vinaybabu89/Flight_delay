import json
import pickle
import numpy as np

__AIRLINE = None
__ORIGIN_AIRPORT = None
__DESTINATION_AIRPORT = None
__data_columns = None
__model = None


def get_flight_delay(AIRLINE, ORIGIN_AIRPORT, DESTINATION_AIRPORT, MONTH, DAY, DAY_OF_WEEK, SCHEDULED_DEPARTURE,
                     DEPARTURE_TIME, DEPARTURE_DELAY, TAXI_OUT, SCHEDULED_ARRIVAL):
    try:
        airline_index = __data_columns.index(AIRLINE.lower())
        origin_index = __data_columns.index(ORIGIN_AIRPORT.lower())
        destination_index = __data_columns.index(DESTINATION_AIRPORT.lower())

    except:

        airline_index = -1
        origin_index = -1
        destination_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = MONTH
    x[1] = DAY
    x[2] = DAY_OF_WEEK
    x[3] = SCHEDULED_DEPARTURE
    x[4] = DEPARTURE_TIME
    x[5] = DEPARTURE_DELAY
    x[6] = TAXI_OUT
    x[7] = SCHEDULED_ARRIVAL
    if airline_index >= 0:
        x[airline_index] = 1

    if origin_index >= 0:
        x[origin_index] = 1

    if destination_index >= 0:
        x[destination_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __AIRLINE
    global __ORIGIN_AIRPORT
    global __DESTINATION_AIRPORT

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __AIRLINE = __data_columns[8:21]
        __ORIGIN_AIRPORT = __data_columns[22:343]
        __DESTINATION_AIRPORT = __data_columns[344:665]

    global __model
    if __model is None:
        with open('./artifacts/USflight_delay_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_airline_name():
    return __AIRLINE


def get_origin_name():
    return __ORIGIN_AIRPORT


def get_destination_name():
    return __DESTINATION_AIRPORT


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_airline_name())
    print(get_origin_name())
    print(get_destination_name())
    print(get_flight_delay('AS', 'ANC', 'SEA', 1, 4, 2, 1252, 1247.0, -5.0, 14.0, 1429))
    # print(get_flight_delay(4, 4, 4, 1200, 1400.0, -11.0, 24.0, 1450, 'AS', 'ANC', 'SEA'))
