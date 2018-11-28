#####################
# ECE 4900 - Team 3         #
#                                          #
# File: weightSensorGui.py #
####################

from guizero import App, Text, TextBox, PushButton, yesno
import subprocess as sub
import os
import signal
import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711

# Globals
hx = HX711(dout=5, pd_sck=6)

DUMMY_SENSOR_OVER = 200
DUMMY_SENSOR_UNDER = 200

# Functions
def weight_set_success():
	weight_enter_message.value = "Weight Successfully Set: " + user_weight_box.value + " lbs\n"
	#print(val)

	if (DUMMY_SENSOR_OVER > int(user_percent_box.value)/100 * int(user_weight_box.value)): # over case
		gui.bg = "red"
	elif (DUMMY_SENSOR_UNDER <= int(user_percent_box.value)/100 * int(user_weight_box.value)): # under case
		gui.bg = "lightgreen"

#percent set success
def percent_set_success():
	weight_percentage_message.value = "Percentage Successfully Set: " + user_percent_box.value + " %\n"	


	if (DUMMY_SENSOR_OVER > int(user_percent_box.value)/100 * int(user_weight_box.value)): # over case
		gui.bg = "red"
	elif (DUMMY_SENSOR_UNDER <= int(user_percent_box.value)/100 * int(user_weight_box.value)): # under case
		gui.bg = "lightgreen"

def poll_example():
	stream.value="Current value: "+ str(10 * hx.getWeight())

def close_message():
	if yesno("Close", "Are you sure you would like to quit weight sensor?"):
		gui.destroy()


#def over_or_under():
#	if (DUMMY_SENSOR_OVER > 0.2 * user_weight_box.value): # over case
#		over_alert = Text(gui, text="Too fat!", size=8, font="Times New Roman", color="red")
#	elif (DUMMY_SENSOR_UNDER <= 0.2 * user_weight_box.value): # under case
#		under_alert = Text(gui, text="Too skinny!", size=8, font="Times New Roman", color="green")

# MAIN #
hx.setReferenceUnit(3.023)

hx.reset()
hx.tare()

# Fork keyboard process
proc = sub.Popen("matchbox-keyboard", shell=True, stdout=sub.PIPE, stderr=sub.PIPE)

# Main GUI Script
	#BEGIN
gui = App(title="Weight Sensor", height=240, width=320)

welcome_message = Text(gui, text="Welcome to Team 3's Weight Sensor", size=16, font="Times New Roman")
weight_enter_message = Text(gui, text="Please Enter Your Weight Below\n", size=13, font="Times New Roman", color="blue")

user_weight_box = TextBox(gui, width=30)
set_button = PushButton(gui, text="Set Weight (lbs)", command=weight_set_success)

# Example Stream
stream = Text(gui)
stream.repeat(500, poll_example) # display value from hx every 0.5 seconds

#Weight Percentage
weight_percentage_message = Text(gui, text="Please Enter Weight Percentage\n", size=13, font="Times New Roman", color="blue")

user_percent_box = TextBox(gui, width=30)
set_button = PushButton(gui, text="Set Percentage (0-100%)", command=percent_set_success)

	#END
gui.on_close(close_message)

gui.display()

GPIO.cleanup()
sys.exit()
os.killpg(os.getpgid(proc.pid), signal.SIGTERM)

