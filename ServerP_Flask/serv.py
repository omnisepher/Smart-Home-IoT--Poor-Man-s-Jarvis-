from flask import Flask,render_template,jsonify,request, Response
from api.tempAndHum import pigdht as pigd
from api.gas import gassense as gas
from api.light import lightsense as light
import datetime
from time import sleep
import cv2
import sys
import numpy
import RPi.GPIO as GPIO
import os
import time

app = Flask(__name__)


@app.route('/TAH',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        tempX, humX = pigd.read()
        # print('Temperature ; ' + str(tempX) + ' Humidity ; ' + str(humX))
        return jsonify({"temperature": tempX, "humidity": humX})
    if request.method == 'POST':
        data = request.get_json()
        command = data['set']
        pigd.comset(command)
        return jsonify({'result' : 'temp device is '+str(command)})


alarm = 37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(alarm,GPIO.OUT)

@app.route('/gas',methods=['GET','POST'])
def gasData():
    if request.method == 'GET':
        gasX = gas.read()
        if gasX == 0:
            GPIO.output(alarm, True)
            time.sleep(.5)
            GPIO.output(alarm, False)
            time.sleep(.5)
        GPIO.output(alarm,False)
        # print('Temperature ; ' + str(tempX) + ' Humidity ; ' + str(humX))
        # print (gasX)
        return jsonify({"gas": gasX})
    if request.method == 'POST':
        data = request.get_json()
        command = data['set']
        gas.comset(command)
        return jsonify({'result': 'gas device is '+str(command)})


lightpow = 40

GPIO.setup(lightpow, GPIO.OUT, initial=GPIO.LOW)

@app.route('/light',methods=['GET','POST'])
def lightData():
    threshold = 0
    auto = 0
    if request.method == 'GET':
        lightX = light.read()
        if auto == 1:
            if lightX > threshold:
                GPIO.output(lightpow, GPIO.HIGH)
            else:
                GPIO.output(lightpow, GPIO.LOW)
        # print('Temperature ; ' + str(tempX) + ' Humidity ; ' + str(humX))
        # print(lightX)
        return jsonify({"light": lightX})
    if request.method == 'POST':
        data = request.get_json()
        command = data['set']
        threshold = data['thresh']
        auto= data['auto']
        light.comset(command)
        print(data)
        return jsonify({'result': 'light device is '+str(command)})


############

@app.route('/cam')
def cam():
    return render_template('index.html')


def get_frame():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)  # this makes a web cam object
    camera.set(3, 320)
    camera.set(4, 240)
    while True: 
        retval, im = camera.read()
        imgencode = cv2.imencode('.jpg', im)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')

    del(camera)


@app.route('/calc')
def calc():
     return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

#
#
#
#

# @app.route('/doorcam')
# def doorcam():
#     return render_template('index2.html')


# def get_frame2():
#     camera_port2 = 1
#     camera2 = cv2.VideoCapture(camera_port2)  # this makes a web cam object
#     camera2.set(3, 320)
#     camera2.set(4, 240)
#     while True:
#         retval2, im2 = camera2.read()
#         imgencode2 = cv2.imencode('.jpg', im2)[1]
#         stringData2 = imgencode2.tostring()
#         yield (b'--frame\r\n'
#                b'Content-Type: text/plain\r\n\r\n'+stringData2+b'\r\n')

#     del(camera2)


# @app.route('/calc2')
# def calc2():
#      return Response(get_frame2(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True,port=5555)
