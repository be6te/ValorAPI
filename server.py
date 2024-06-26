from flask import Flask, jsonify, request
from VALORANT.Convert import Converter
d = Converter()

app = Flask(__name__)

@app.route('/')
def wlc():
    return '/api/valorant/seasons'

@app.route('/api/valorant/seasons')
def api():
    return jsonify(d.get_seasons(name='bet#898'))

app.run()