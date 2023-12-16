import sys
import runpy

path_arm = 'lumino_car/Arm.py'
# path_car = 'lumino_car/Car.py'

mode = sys.argv.pop(1)

if mode == 'arm':
    runpy.run_path(path_arm, run_name='__main__')
else:
    print(f'Unknown mode: {mode}')
    sys.exit(1)