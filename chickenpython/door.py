#!/usr/bin/env python
# coding=UTF-8

import RPi.GPIO as gpio
import datetime
import time
import logging

TIME_CLOSE = 100
TIME_OPEN = 83
FILENAME = "/opt/chickendoor/status.txt"
LOGFILE = "/opt/chickendoor/chicken.log"

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    logging.basicConfig(filename='chicken.log', level=logging.DEBUG, format='%(asctime)s — %(name)s — %(levelname)s — %(message)s')


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
        gpio.output(17, True)
        gpio.output(22, False)
        time.sleep(TIME_CLOSE)
        gpio.cleanup()
        logging.info("DOOR Opened !")
        write_status("Opened")
    else:
        gpio.cleanup()
        logging.warning("ERROR! Action OPEN but door not closed!")


def force_open_door():
    force_open_door_duration(TIME_OPEN)

def force_open_door_duration(parDuration):
    write_status("Opening")
    logging.info("DOOR FORCED Opening…")
    gpio.output(17, True)
    gpio.output(22, False)
    time.sleep(parDuration)
    gpio.cleanup()
    logging.info("DOOR FORCED Opened!")
    write_status("Opened")


def close_door():
    if read_status() == "Opened":
        write_status("Closing")
        logging.info("DOOR Closing…")
        gpio.output(17, False)
        gpio.output(22, True)
        time.sleep(TIME_OPEN)
        gpio.cleanup()
        logging.info("DOOR Closed!")
        write_status("Closed")
    else:
        gpio.cleanup()
        logging.warning("ERROR! Action CLOSE but door not opened!")


def force_close_door():
    force_close_door_duration(TIME_CLOSE)

def force_close_door_duration(parDuration):
    write_status("Closing")
    logging.info("DOOR FORCED Closing…")
    gpio.output(17, False)
    gpio.output(22, True)
    time.sleep(parDuration)
    gpio.cleanup()
    logging.info("DOOR FORCED Closed!")
    write_status("Closed")
