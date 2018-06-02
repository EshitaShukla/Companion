#! /usr/bin/env python

from flask import Flask, render_template, url_for, request, session, redirect, send_from_directory, jsonify
import os
import serial
import time

ArduinoSerial = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)

app = Flask(__name__)

@app.route('/control')
def control():
    json_form = json.loads(request.json)
    data = str(json_form['data']).encode('utf-8')
    ArduinoSerial.write(bytes(data))
    return 'ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
