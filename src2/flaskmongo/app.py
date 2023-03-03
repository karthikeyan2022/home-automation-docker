from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import sys
import os
app = Flask(__name__)

client = MongoClient("mongodb+srv://raspberrypi_docker_user:raspberrypi@cluster0-tgb3y.mongodb.net/test?retryWrites=true")
db = client.project
collection = db.sensors
collection.delete_many({})

collection.insert_one( { "id": 1, "name": "temperature", "value": "null" } )
collection.insert_one( { "id": 2, "name": "moisture", "value": "water not detected" } )
collection.insert_one( { "id": 3, "name": "ldr", "value": "light off" } )

@app.route('/', methods=['GET'])
def home():
    return """<h1>Sensor Reading </h1>
    <p>A API for sensor reading in raspberry pi</p>
    """

@app.errorhandler(404)
def page_not_found(e):
    return """<h1>Error 404: File not found</h1>"""

# A route to return all of the available entries in our catalog.
@app.route('/sensors', methods=['GET'])
def api_all():
    data = collection.find()
    return render_template('index.html', data = data)





if __name__ == '__main__':

    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

