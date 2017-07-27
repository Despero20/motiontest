from gpiozero import MotionSensor,LED#Button
from signal import pause
import urllib2
pir = MotionSensor(4)
led = LED(17)
#button=Button(1)
#def dot():
#	led.on()
#	led.off()

def iftt():
	led.on()
	urllib2.urlopen("https://maker.ifttt.com/trigger/motiontest/with/key/g0woufvAOWmL0-vISwBnF7PQ3wMsZ0SNZ1Nblazz-2r")

#def intruder():
# print ("intruder")


while True:
	#pir.when_motion =led.on

	pir.when_motion = iftt
#	pir.when_motion=intruder
#pir.when_no_motion = led.off
#elif button.when_pressed:

#pir.when_motion=iftt

#Oelse:
	pir.when_no_motion=led.off

pause()

#from gpiozero import MotionSensor

#pir = MotionSensor(4)
#while True:
    #if pir.motion_detected:
        #print("Motion detected!")
