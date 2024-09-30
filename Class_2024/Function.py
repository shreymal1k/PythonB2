# Write a program to estimate rintime of all the function you have used so far.


import time as t
from functionScope import add as fn1

def testFn():
    pass

startTime =t.time()
testFn()
endTime=t.time()
runTimeInSec = endTime - startTime 
print(f"\n Time to execute function is {runTimeInSec/60} min")   

result =fn1(5,3)
print(result) # Output:8

# Modify all your previous funtions ti print there execution time
# create a presentation and 