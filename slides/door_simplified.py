from gpiozero import Motor
from gpiozero import Button
import time

TIME_CLOSE = 99
TIME_OPEN = 69
motor = Motor(forward=17, backward=22)
button = Button(2)

button.when_pressed = info_button_pressed

def open_door():
    motor.forward()
    time.sleep(TIME_OPEN)
    motor.stop()

def close_door():
    time_spent=0
    motor.backward()
    while not button.is_pressed and time_spent<TIME_CLOSE:
      time.sleep(1)
      time_spent+=1
    motor.stop()
