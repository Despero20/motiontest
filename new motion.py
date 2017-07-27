from gpiozero import LED, Button
from signal import pause
import urllib2
from gpiozero import MotionSensor

pir = MotionSensor(4)
led = LED(17)
button=Button(27)

def ifttt():
      print "done"
      urllib2.urlopen("https://maker.ifttt.com/trigger/button_pressed/with/key/hBgwVN2raqAmjrPLQIULaTWbAejD8fYJipCyiKL3jlC").read

When_button_pressed = led.on

def on_pressed():
	if pir.motion.detected:
		led.on
	else:
		ifttt()

