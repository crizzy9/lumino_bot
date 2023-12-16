#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/spadia/lumino_bot/lumino/')
import time
import signal
import threading
import HiwonderSDK.Board as Board

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    
print('''
**********************************************************
********Function: Magic Technology Raspberry Pi expansion board, PWM steering gear control routine**********
**********************************************************
----------------------------------------------------------
Official website:https://www.hiwonder.com
Online mall:https://hiwonder.tmall.com
----------------------------------------------------------
Tips:
 * Press Ctrl+C to turn off this program. If you fail, try many times!
----------------------------------------------------------
''')

start = True
#Treatment before turning off
def Stop(signum, frame):
    global start

    start = False
    print('Closure...')

signal.signal(signal.SIGINT, Stop)

if __name__ == '__main__':
    
    while True:
        Board.setPWMServoPulse(1, 1500, 1000) # Set the pulse of No. 1 rudder to 1500, and the running time is 1000 milliseconds
        time.sleep(1)
        Board.setPWMServoPulse(1, 2500, 1000) # Set the pulse width of the 1st rudder to 2500, and the running time is 1000 milliseconds
        time.sleep(1)
        
        if not start:
            Board.setPWMServoPulse(1, 1500, 1000) # Set the pulse of No. 1 rudder to 1500, and the running time is 1000 milliseconds
            time.sleep(1)
            print('已关闭')
            break
    
    
        