from flask import Flask, render_template, request, json, jsonify
from flask_googlemaps import GoogleMaps, Map
from lib.api.zoning import Q2J

#import json

app = Flask(__name__, template_folder="./templates")


app.config['GOOGLEMAPS_KEY'] = "AIzaSyAgZDoXzJBhfIq--DbQTfCLutn9r_OyRjo"
GoogleMaps(app)

@app.route('/')
def mapview():
    return render_template('mapframe.html')


@app.route('/get_map')
def get_map():

    return render_template('googlemap.html')

@app.route('/crime_data', methods= ['GET', 'POST'])
def get_crime_data():
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        info = request.json
        print(info)
        return jsonify(info)
    else:
        return render_template('mapframe.html')
    #query = Q2J.QueryToJSON()
    #query.load_data_frame('/Users/galil/src/crime_mapper/lib/api/zoning/2017assault.csv')
    #data = query.make_percentile_map()


if __name__ == "__main__":
    app.run(debug=True)

