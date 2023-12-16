#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/spadia/masterpi-car/lumino/')
import time
import signal
import threading
import HiwonderSDK.Board as Board

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    
print('''
**********************************************************
********Function: Magic Technology Raspberry Pi expansion board, motor control routine**********
**********************************************************
----------------------------------------------------------
Official website:https://www.hiwonder.com
Online mall:https://hiwonder.tmall.com
----------------------------------------------------------
Tips:
 * Press Ctrl+C to turn off this program. If you fail, try many times!
----------------------------------------------------------
''')

# Turn off all motors
def MotorStop():
    Board.setMotor(1, 0) 
    Board.setMotor(2, 0)
    Board.setMotor(3, 0)
    Board.setMotor(4, 0)

start = True
#Treatment before turning off
def Stop(signum, frame):
    global start

    start = False
    print('Closure...')
    MotorStop()  # Turn off all motors
    

signal.signal(signal.SIGINT, Stop)

if __name__ == '__main__':
    
    while True:
        Board.setMotor(1, 35)  #Set No. 1 motor speed 35
        time.sleep(1)
        Board.setMotor(1, 60)  #Set the speed of No. 1 motor 60
        time.sleep(2)
        Board.setMotor(1, 90)  #Set the speed of No. 1 motor 90
        time.sleep(3)    
        
        if not start:
            MotorStop()  # Turn off all motors
            print('closed')
            break
    
    
        