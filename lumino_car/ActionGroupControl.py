#!/usr/bin/env python3
# encoding: utf-8
import os
import time
import threading
import sqlite3 as sql
from SetPWMServo import *
sys.path.append('/home/spadia/masterpi-car/lumino/')
import yaml_handle

runningAction = False
stopRunning = False

def stop_action_group():
    global stopRunning
    
    stopRunning = True

def runAction(actNum):
    '''
    Operating the action group, you cannot send the STOP stop signal
    :param actNum: The name of the action group, the string type
    :param times:  Number of runs
    :return:
    '''
    global runningAction
    global stopRunning
    global online_action_times
    if actNum is None:
        return
    actNum = "/home/spadia/masterpi-car/lumino/ActionGroups/" + actNum + ".d6a"
    stopRunning = False
    if os.path.exists(actNum) is True:
        if runningAction is False:
            runningAction = True
            ag = sql.connect(actNum)
            cu = ag.cursor()
            cu.execute("select * from ActionGroup")
            deviation_data = yaml_handle.get_yaml_data(yaml_handle.Deviation_file_path)
            while True:
                act = cu.fetchone()
                if stopRunning is True:
                    stopRunning = False                   
                    break
                if act is not None:
                    setPWMServosPulse([ act[1], 5, 1,act[2] + deviation_data['1'],
                                                   3,act[3] + deviation_data['3'],
                                                   4,act[4] + deviation_data['4'],
                                                   5,act[5] + deviation_data['5'],
                                                   6,act[6] + deviation_data['6']])
                    if stopRunning is True:
                        stopRunning = False                   
                        break
                    time.sleep(float(act[1])/1000.0)
                else:   # Exit only after running
                    break
            runningAction = False
            
            cu.close()
            ag.close()
    else:
        runningAction = False
        print("No action group found")
