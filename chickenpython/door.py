#!/usr/bin/env python
# coding=UTF-8

from gpiozero import Motor
from gpiozero import Button
import datetime
import time
import logging

TIME_CLOSE = 100
TIME_OPEN = 83
FILENAME = "/opt/chickendoor/status.txt"
LOGFILE = "/opt/chickendoor/chicken.log"
motor = Motor(forward=17, backward=22)
button = Button(2)

def init():
    logging.basicConfig(filename='chicken.log', level=logging.DEBUG, format='%(asctime)s — %(name)s — %(levelname)s — %(message)s')


def say_hello():
    logging.info("Door button pressed")

button.when_pressed = say_hello

def read_status():
    file = open(FILENAME, "r")
    status = file.readline()
    file.close()
    return(status)


def write_status(STATUS):
    file = open(FILENAME, "w")
    file.write(STATUS)
    file.close()


def open_door():
    if read_status() == "Closed":
        write_status("Opening")
        logging.info("DOOR Opening…")
        motor.forward()
        time.sleep(TIME_CLOSE)
        motor.stop()
        logging.info("DOOR Opened !")
        write_status("Opened")
    else:
        logging.warning("ERROR! Action OPEN but door not closed!")


def force_open_door():
    force_open_door_duration(TIME_OPEN)

def force_open_door_duration(parDuration):
    write_status("Opening")
    logging.info("DOOR FORCED Opening…")
    motor.forward()
    time.sleep(parDuration)
    motor.stop()
    logging.info("DOOR FORCED Opened!")
    write_status("Opened")


def close_door():
    if read_status() == "Opened":
        write_status("Closing")
        logging.info("DOOR Closing…")
        motor.backward()
        time_spent=0
        while not button.is_pressed and time_spent<TIME_CLOSE:
          time.sleep(1)
          time_spent+=1
          logging.info ("time spent: " +str(time_spent))
        motor.stop()
        logging.info("DOOR Closed!")
        write_status("Closed")
    else:
        logging.warning("ERROR! Action CLOSE but door not opened!")


def force_close_door():
    force_close_door_duration(TIME_CLOSE)

def force_close_door_duration(parDuration):
    write_status("Closing")
    logging.info("DOOR FORCED Closing…")
    motor.backward()
    time.sleep(parDuration)
    motor.stop()
    logging.info("DOOR FORCED Closed!")
    write_status("Closed")
