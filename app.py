from flask import Flask, render_template, request, json, jsonify
from flask_googlemaps import GoogleMaps, Map
from lib.api.zoning import Q2J
from lib.api.zoning.bin.QueryCrimeTable import QueryCrimeTable


import json

JSON_info = None
info = None

app = Flask(__name__, template_folder="./templates")


app.config['GOOGLEMAPS_KEY'] = "AIzaSyAgZDoXzJBhfIq--DbQTfCLutn9r_OyRjo"
GoogleMaps(app)

@app.route('/')
def startview():
    return render_template('start_map.html')

@app.route('/mapview')
def mapview():
    return render_template('mapframe.html')


@app.route('/get_map')
def get_map():

    return render_template('googlemap.html', info=JSON_info)

@app.route('/crime_data', methods= ['GET', 'POST'])
def get_crime_data():
    global info
    if request.method == 'POST':
        global JSON_info
        info = request.json
        crime = info['crime'].strip()
        start_date = str(info['start'][:10].replace('-', ''))
        end_date = str(info['end'][:10].replace('-', ''))

        print("Crime: {}, start_date: {}, end_date: {}"
                            .format(crime, start_date, end_date))
        query = QueryCrimeTable()
        JSON_info = query.get_crime_json(start_date, end_date, crime)
        return jsonify(info)
    else:
        print("This is else in flask: ", info)
        return render_template('googlemap.html');

@app.route('/get_data', methods = ['GET'])
def get_data():
    return jsonify(info)

@app.route('/group_info', methods = ['GET'])
def group_info():
    return render_template('bio.html')


@app.route('/start_map', methods= ['GET'])
def start_map():
    return render_template('chicagomap.html')

if __name__ == "__main__":
    app.run(debug=True)

