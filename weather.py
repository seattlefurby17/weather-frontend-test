import logging
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import requests
import os
from dotenv import load_dotenv
load_dotenv()
apiKey = os.getenv('API_KEY')
baseUrl = 'https://api.openweathermap.org/data/2.5/'

app = Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/temperature', methods=['GET'])
@cross_origin()
def temperature():
  currentCity = request.args.get('currentCity')
  r = requests.get(baseUrl + 'weather?q='+currentCity+'&units=imperial&appid='+apiKey+'')
  return r.json()

@app.route('/forecast', methods=['GET'])
@cross_origin()
def forecast():
  currentCity = request.args.get('currentCity')
  r = requests.get(baseUrl + 'forecast?q='+currentCity+'&units=imperial&appid='+apiKey+'')
  return r.json()


if __name__ == '__main__':
  app.run(debug=True)