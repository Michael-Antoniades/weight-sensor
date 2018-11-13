#####################
# ECE 4900 - Team 3         #
#                                          #
# File: weightSensorGui.py #
####################

from guizero import App, Text, TextBox, PushButton

# Globals
DUMMY_SENSOR_OVER = 360.0
DUMMY_SENSOR_UNDER = 20.0


# Functions
def weight_set_success():
	weight_enter_message.value = "Weight Successfully Set: " + user_weight_box.value + " lbs\n"

	if (DUMMY_SENSOR_OVER > 0.2 * int(user_weight_box.value)): # over case
		gui.bg = "red"
	elif (DUMMY_SENSOR_UNDER <= 0.2 * int(user_weight_box.value)): # under case
		gui.bg = "lightgreen"

def over_or_under():
	if (DUMMY_SENSOR_OVER > 0.2 * user_weight_box.value): # over case
		over_alert = Text(gui, text="Too fat!", size=16, font="Times New Roman", color="red")
	elif (DUMMY_SENSOR_UNDER <= 0.2 * user_weight_box.value): # under case
		under_alert = Text(gui, text="Too skinny!", size=16, font="Times New Roman", color="green")


# Main GUI Script
gui = App(title="Weight Sensor", height=800, width=800)

welcome_message = Text(gui, text="Welcome to Team 3's Weight Sensor", size=40, font="Times New Roman")
weight_enter_message = Text(gui, text="Please Enter Your Weight Below\n", size=26, font="Times New Roman", color="blue")

user_weight_box = TextBox(gui, width=30)
set_button = PushButton(gui, text="Set Weight (lbs)", command=weight_set_success)

gui.display()

