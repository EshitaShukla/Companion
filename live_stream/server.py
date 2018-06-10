#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2
import socket
import io

# Define the cameras
vc = cv2.VideoCapture(0)

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming"""
    return render_template('index.html')

def gen_zero():
    """Video streaming generator function."""
    while True:
        rval, frame = vc.read()
        cv2.imwrite('t.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')

@app.route('/video_feed_zero')
def video_feed_zero():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_zero(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=2409, debug=True, threaded=True)
               
