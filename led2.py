from gpiozero import LED

from time import sleep


led = LED(17)

def dot():
	led.on()
	sleep(1)
	led.off()

def dash():
	led.off()
	sleep(5)
	led.on()
	sleep(5)
	led.off


if __name__=='__main__':
	dot()
	dash()
	dot()
