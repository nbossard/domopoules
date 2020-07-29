#!/usr/bin/env python
# coding=UTF-8

from gpiozero import Button


#the door close detection button is on GPIO2
button = Button(2)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
