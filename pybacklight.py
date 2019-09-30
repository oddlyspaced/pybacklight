#!/bin/python3
import subprocess
import sys

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

def set_backlight(brightness) :
    current_brightness = int(str(subprocess.check_output("cat /sys/class/backlight/amdgpu_bl0/brightness", shell=True))[2:-3])
    print("cur : " + str(current_brightness))
    brightness = str(brightness)
    print("bri : " + str(brightness))
    if (brightness.startswith("+") or brightness.startswith("-")) :
        brightness = current_brightness + int(brightness)
    subprocess.call("echo \"" + str(brightness) + "\" > /sys/class/backlight/amdgpu_bl0/brightness", shell=True)

parse_arg()
