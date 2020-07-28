#!/usr/bin/env python
# coding=UTF-8

from gpiozero import Motor
from gpiozero import Button
import datetime
import time
import logging

TIME_CLOSE = 99
TIME_OPEN = 65
FILENAME = "/opt/chickendoor/status.txt"
LOGFILE = "/opt/chickendoor/chicken.log"
motor = Motor(forward=17, backward=22)
button = Button(2)

def init():
    logging.basicConfig(filename='chicken.log', level=logging.DEBUG, format='%(asctime)s — %(name)s — %(levelname)s — %(message)s')

def print_and_log(message): 
    logging.info(message)
    print message

def info_button_pressed():
    print_and_log("Door button pressed")

button.when_pressed = info_button_pressed

def read_status():
    file = open(FILENAME, "r")
    status = file.readline()
    file.close()
    return(status)


def write_status(STATUS):
    file = open(FILENAME, "w")
    print_and_log("Writing new status: " + STATUS)
    file.write(STATUS)
    file.close()


def open_door():
    if read_status() == "Closed":
        write_status("Opening")
        print_and_log("DOOR Opening…")
        motor.forward()
        time.sleep(TIME_CLOSE)
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
        close_autostop()
        print_and_log("DOOR Closed!")
    else:
        logging.warning("ERROR! Action CLOSE but door not opened!")


def force_close_door():
    force_close_door_duration(TIME_CLOSE)

def force_close_door_duration(parDuration):
    print_and_log("DOOR FORCED Closing…")
    close_autostop()
    print_and_log("DOOR FORCED Closed!")

def close_autostop()
    write_status("Closing")
    time_spent=0
    motor.backward()
    while not button.is_pressed and time_spent<TIME_CLOSE:
      time.sleep(1)
      time_spent+=1
      print_and_log ("time spent: " +str(time_spent))
    motor.stop()
    write_status("Closed")
