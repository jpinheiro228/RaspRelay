from flask import Flask
import RPi.GPIO as GPIO
from time import sleep
import logging

app = Flask(__name__)

# Disable Logging on terminal
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

# Setup the GPIO Pins
GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 2
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.output(RELAIS_1_GPIO, GPIO.LOW)


@app.route('/reset')
def reset():
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    sleep(5)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    return "Done!"


@app.route('/on')
def set_on():
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    return "Done!"


@app.route('/off')
def set_off():
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    return "Done!"


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
