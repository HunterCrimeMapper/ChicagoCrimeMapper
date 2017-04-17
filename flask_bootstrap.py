from flask import Flask, render_template
from flask_googlemaps import GoogleMaps, Map

from flask_bootstrap import flask_bootstrap


def create_app():
    app = Flask(__name__, template_folder="./templates")
    Bootstrap(app)


app.config['GOOGLEMAPS_KEY'] = "AIzaSyAgZDoXzJBhfIq--DbQTfCLutn9r_OyRjo"
GoogleMaps(app)

@app.route('/')
def mapview():
    return render_template('flask_bootstrap_test.html')
    #return render_template('OSM_bootstrap.html', fullmap=fullmap)

#@app.route('/get_map')
#def get_map():
#    return render_template('new_html.html')

if __name__ == "__main__":
    app.run(debug=True)

