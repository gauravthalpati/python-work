# This is the code which has a function (sleep_awhile) & another dependent
# function time.sleep
# In this exercise we will mock time.sleep

# Reference
# https://blogs.sap.com/2022/02/16/how-to-write-independent-unit-test-with-pytest-and-mock-techniques/

import time

def sleep_awhile(duration):
    print ("sleep function is getting executed")
    time.sleep(duration)
    print("sleep function COMPLETED")

#print("Sleeping...")
#sleep_awhile(10)
#print("Done...")

