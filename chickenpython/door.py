#!/usr/bin/env python3
# coding=UTF-8

from gpiozero import Motor
from gpiozero import Button
import datetime
import time
import logging
import re

TIME_CLOSE = 99
TIME_OPEN = 69
STATUSFILENAME = "/home/pi/domopoules/chickenpython/status.txt"
motor = Motor(forward=17, backward=22)
button = Button(2)

def init():
    logging.basicConfig(filename='chicken.log', level=logging.DEBUG, format='%(asctime)s — %(name)s — %(levelname)s — %(message)s')

def print_and_log(message): 
    logging.info(message)
    print(message)

def info_button_pressed():
    print_and_log("Door button pressed")

button.when_pressed = info_button_pressed

def read_status():
    file = open(STATUSFILENAME, "r")
    status = file.readline()
    # remove potential noise such as newline
    status = re.sub(r"[\n\t\s]*", "", status)
    file.close()
    print_and_log("Current status is: -->" + status + "<--")
    return(status)


def write_status(STATUS):
    file = open(STATUSFILENAME, "w")
    print_and_log("Writing new status: " + STATUS)
    file.write(STATUS)
    file.close()


def open_door():
    if read_status() == "Closed":
        write_status("Opening")
        print_and_log("DOOR Opening…")
        motor.forward()
        time.sleep(TIME_OPEN)
        motor.stop()
        print_and_log("DOOR Opened !")
        write_status("Opened")
    else:
        logging.warning("ERROR! Action OPEN but door not closed!")


def force_open_door():
    force_open_door_duration(TIME_OPEN)

def force_open_door_duration(parDuration):
    write_status("Opening")
    print_and_log("DOOR FORCED Opening…")
    motor.forward()
    time.sleep(parDuration)
    motor.stop()
    print_and_log("DOOR FORCED Opened!")
    write_status("Opened")


def close_door():
    if read_status() == "Opened":
        print_and_log("DOOR Closing…")
        close_autostop(TIME_CLOSE)
        print_and_log("DOOR Closed!")
    else:
        logging.warning("ERROR! Action CLOSE but door not opened!")


def force_close_door():
    force_close_door_duration(TIME_CLOSE)

def force_close_door_duration(parDuration):
    print_and_log("DOOR FORCED Closing…")
    close_autostop(parDuration)
    print_and_log("DOOR FORCED Closed!")

def close_autostop(parDuration):
    write_status("Closing")
    time_spent=0
    motor.backward()
    while not button.is_pressed and time_spent<parDuration:
      time.sleep(1)
      time_spent+=1
      print_and_log ("time spent: " +str(time_spent))
    motor.stop()
    write_status("Closed")
