#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/spadia/masterpi-car/lumino/')
import time
import signal
import HiwonderSDK.mecanum as mecanum

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    
print('''
**********************************************************
*******************Function: Circuit**********************
**********************************************************
----------------------------------------------------------
Official website:https://www.hiwonder.com
Online mall:https://hiwonder.tmall.com
----------------------------------------------------------
Tips:
 * Press Ctrl+C to turn off this program. If you fail, try many times!
----------------------------------------------------------
''')

chassis = mecanum.MecanumChassis()

start = True
#Treatment before turning off
def Stop(signum, frame):
    global start

    start = False
    print('关闭中...')
    chassis.set_velocity(0,0,0)  # Turn off all motors
    

signal.signal(signal.SIGINT, Stop)

if __name__ == '__main__':
    while start:
        chassis.set_velocity(50,90,0)
        time.sleep(1)
        
    chassis.set_velocity(0,0,0)  # Turn off all motors
    print('closed')
        
