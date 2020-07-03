import os
import time

time_start = time.time()
os.system("python3 listdir.py")
os.system("python3 compilefile.py")
os.system("python3 runtest.py")
time_end = time.time()
print('Total time consumed:',time_end - time_start, 's\t\n')
