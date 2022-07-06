#!/usr/bin/env python3
# coding=UTF-8

# refer to doc here : https://gpiozero.readthedocs.io/en/stable/recipes.html#button

from gpiozero import Button


#the door close detection button is on GPIO2
button = Button(2)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
