#!/bin/python3
import subprocess
import sys
from os import listdir
def parse_arg() :
    args = list(sys.argv)
    for arg in args :
        arg = str(arg)
        if arg.startswith("/") :
            continue
        else :
            try :
                set_backlight(arg)
            except Exception as e:
                print("Please enter correct value!")
                print_help()

def set_backlight(brightness) :
    card = get_card()
    current_brightness = int(str(subprocess.check_output("cat /sys/class/backlight/" + card + "/brightness", shell=True))[2:-3])
    brightness = str(brightness)
    if (brightness.startswith("+") or brightness.startswith("-")) :
        brightness = current_brightness + int(brightness)
        if brightness < 0 :
            brightness = 0
        if brightness > get_max_brightness() :
            brightness = get_max_brightness()
    subprocess.call("echo \"" + str(brightness) + "\" > /sys/class/backlight/" + card + "/brightness", shell=True)

# get card returns the first instance of the card it finds
def get_card() :
    return str(list(listdir("/sys/class/backlight"))[0])

def get_max_brightness() :
    return int(str(subprocess.check_output("cat /sys/class/backlight/" + get_card() + "/max_brightness", shell=True))[2:-3])

def print_help() :
    print("usage: <pybacklight> <value>")

parse_arg()
