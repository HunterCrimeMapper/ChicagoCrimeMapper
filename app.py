from flask import Flask, render_template
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__, template_folder="./templates")


app.config['GOOGLEMAPS_KEY'] = "AIzaSyAgZDoXzJBhfIq--DbQTfCLutn9r_OyRjo"
GoogleMaps(app)

@app.route('/')
def mapview():
    fullmap = Map(
        identifier="fullmap",
        lat = 41.8781,
        lng = -87.6298,
        markers =[(41.8781, -87.6298), (41.8783, -87.6398)]
    )
    return render_template('OSM_bootstrap.html')
    #return render_template('OSM_bootstrap.html', fullmap=fullmap)

@app.route('/get_map')
def get_map():
    return render_template('new_html.html')

if __name__ == "__main__":
    app.run(debug=True)

