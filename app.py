from flask import Flask, render_template, request, json, jsonify
from flask_googlemaps import GoogleMaps, Map
from lib.api.zoning import Q2J

import json

info = None

app = Flask(__name__, template_folder="./templates")


app.config['GOOGLEMAPS_KEY'] = "AIzaSyAgZDoXzJBhfIq--DbQTfCLutn9r_OyRjo"
GoogleMaps(app)

@app.route('/')
def mapview():
    return render_template('start_map.html')


@app.route('/get_map')
def get_map():

    return render_template('googlemap.html')

@app.route('/crime_data', methods= ['GET', 'POST'])
def get_crime_data():
    #import pdb; pdb.set_trace()
    #info = None
    if request.method == 'POST':
        global info
        info = request.json
        print("This is in flask: ", info)
        return jsonify(info)
    else:
        print("This is else in flask: ", info)
        return render_template('mapframe.html', info=jsonify(info));
        #return jsonify(info);
    #query = Q2J.QueryToJSON()
    #query.load_data_frame('/Users/galil/src/crime_mapper/lib/api/zoning/2017assault.csv')
    #data = query.make_percentile_map()

@app.route('/get_data', methods = ['GET'])
def get_data():
    return jsonify(info)

@app.route('/start_map', methods=['GET'])
def start_map():
    return render_template('chicagomap.html')

if __name__ == "__main__":
    app.run(debug=True)

