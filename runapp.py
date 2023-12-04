import sys
import runpy

path_arm = 'MasterPi_PC_Software/Arm.py'
# path_car = 'MasterPi_PC_Software/Car.py'

mode = sys.argv.pop(1)

if mode == 'arm':
    runpy.run_path(path_arm, run_name='__main__')
else:
    print(f'Unknown mode: {mode}')
    sys.exit(1)