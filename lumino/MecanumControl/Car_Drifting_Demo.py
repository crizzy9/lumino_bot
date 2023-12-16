#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/spadia/lumino_bot/lumino/')
import time
import signal
import HiwonderSDK.mecanum as mecanum

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    
print('''
**********************************************************
***********Function: Cars drift movement routine**********
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
#关闭前处理
def Stop(signum, frame):
    global start

    start = False
    print('Closure...')
    chassis.set_velocity(0,0,0)  # 关闭所有电机
    

signal.signal(signal.SIGINT, Stop)

if __name__ == '__main__':
    while start:
        chassis.set_velocity(50,180,0.3)
        time.sleep(3)
        chassis.set_velocity(50,0,-0.3)
        time.sleep(3)
    chassis.set_velocity(0,0,0)  # 关闭所有电机
    print('closed')

        
