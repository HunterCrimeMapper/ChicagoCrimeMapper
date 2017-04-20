from flask import Flask, render_template, request, json, jsonify
from flask_googlemaps import GoogleMaps, Map
from lib.api.zoning import Q2J

#import json

app = Flask(__name__, template_folder="./templates")


app.config['GOOGLEMAPS_KEY'] = "AIzaSyAgZDoXzJBhfIq--DbQTfCLutn9r_OyRjo"
GoogleMaps(app)

@app.route('/')
def mapview():
    return render_template('galil2_bootstrap.html')


@app.route('/get_map')
def get_map():

    return render_template('googlemap.html')

@app.route('/crime_data', methods= ['GET', 'POST'])
def get_crime_data():
    #import pdb; pdb.set_trace()
    print("HELLLOOOO!!!")
    info = None
    if request.method == 'POST':
        print("Made it into POST")
        info = request.json
        print(info)
        return jsonify(info)
        #response = app.response_class(
        #    response=json.dumps(info),
        #    status=200,
        #    mimetype='application/json')
    else:
        print("Not ran not in post")
        return ("Hi there")
    #query = Q2J.QueryToJSON(2704)
    #query.load_data_frame('/Users/galil/src/crime_mapper/lib/api/zoning/2017assault.csv')
    #data = query.make_percentile_map()


if __name__ == "__main__":
    app.run(debug=True)

