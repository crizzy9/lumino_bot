from pydualsense import *

def cross_down(state):
    dualsense.light.setColorI(255,0,0) # set touchpad color to red
    print(f'cross {state}')


def circle_down(state):
    dualsense.light.setColorI(0,255,0) # set touchpad color to green
    print(f'circle {state}')


def dpad_down(state):
    dualsense.light.setColorI(0,0,255) # set touchpad color to blue
    print(f'dpad {state}')


def joystick(stateX, stateY):
    print(f'lj {stateX} {stateY}')

# create dualsense
dualsense = pydualsense()
# find device and initialize
dualsense.init()

# add events handler functions
dualsense.cross_pressed += cross_down
dualsense.circle_pressed += circle_down
dualsense.dpad_down += dpad_down
dualsense.left_joystick_changed += joystick

if dualsense.state.L2:
    # set L2 to rigid mode and set force to 100% when pressed
    dualsense.triggerL.setMode(TriggerModes.Rigid)
    dualsense.triggerL.setForce(1, 255)

# read controller state until R1 is pressed
while not dualsense.state.R1:
    ...

# reset controller to default state
dualsense.init()

# close device
dualsense.close()