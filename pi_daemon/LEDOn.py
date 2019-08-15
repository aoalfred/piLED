#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from flask import Flask
from flask_restful import Resource, Api
import daemon

app = Flask(__name__)
api = Api(app)

def main_body():
    def initHW():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)

    class Lighton(Resource):
        def get(self):
            if not GPIO.input(18):
                GPIO.output(18, True)
            else:
                GPIO.output(18, False)
                return "LED toggled"

    api.add_resource(Lighton, '/lighton')
    initHW()

    if __name__ == '__main__':
        app.run(host='0.0.0.0',port='5002')

def run():
    with daemon.DaemonContext():
        main_body()

if __name__ == "__main__":
    run()
