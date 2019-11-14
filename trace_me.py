#Norma
#trace_me.py
# H3-5: run the following in the PyCharm debugger and print
#       the following requested info...
import math
num = int(input("enter number of floats: "))

global_max = -1*(math.inf) #should initialize this to negative infinity so that the first input is always larger
global_min = math.inf #initialize to infinity so first input is always smaller
sum = 0.0

for d in range(num):
    e = float(input("enter next float: "))
    global_max = max(global_max, e)
    global_min = min(global_min, e)
    sum = sum + e
    print ("set breakpoint here...")
    # LOCATION 1:
    # 1st:   global_max = 1.0, global_min = 0.0, sum = 1.0, d = 0, e = 1.0
    # 2nd:   global_max = 1.0, global_min = -2.0, sum = -1.0, d = 1, e = -2.0
    # 3rd:   global_max = 3.0, global_min = -2.0, sum = 2.0, d = 2, e = 3.0
    # 4th:   global_max = 3.0, global_min = -4.0, sum = -2.0, d = 3, e = -4.0
    # 5th:   global_max = 5.0, global_min = -4.0, sum = 3.0, d = 4, e = 5.0
    # list values of global_max, global_min, sum, d, e at this point, each time through loop

print (global_max)  #the maximum of all inputs
print (global_min)  #the minimum of all inputs
print (sum / num) #print the average of all inputs

print ("set another breakpoint here...")
# LOCATION 2:
# list final values of global_max, global_min, sum, d, e
# final:   global_max = 5.0, global_min = -4.0, sum = 3.0, d = 4, e = 5.0