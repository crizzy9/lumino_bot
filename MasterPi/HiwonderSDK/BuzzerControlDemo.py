import time
import Board

print('''
**********************************************************
********Function: Magic Technology Raspberry Pi expansion board, bee ring control routine*********
**********************************************************
----------------------------------------------------------
Official website:https://www.hiwonder.com
Online mall:https://hiwonder.tmall.com
----------------------------------------------------------
Tips:
 * Press Ctrl+C to turn off this program. If you fail, try many times!
----------------------------------------------------------
''')

Board.setBuzzer(0) # closure

Board.setBuzzer(1) # Open
time.sleep(0.1) # Delay
Board.setBuzzer(0) #closure

time.sleep(1) # Delay

Board.setBuzzer(1)
time.sleep(0.5)
Board.setBuzzer(0)