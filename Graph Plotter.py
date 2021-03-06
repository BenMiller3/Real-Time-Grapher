# imports matplotlib to graph
import matplotlib.pyplot as plt
import time
import random
from collections import deque
import numpy as np
import datetime

# simulates input from serial port
def random_gen():
    while True:
        val = random.randint(1,100)
        yield val
        time.sleep(0.1)


# matplot lib graphing
a1 = deque([0]*100)
ax = plt.axes(xlim=(0, 20), ylim=(0, 100))
d = random_gen()

# sets line attributes
line, = plt.plot(a1,linewidth=4)
plt.ion()
plt.ylim([0,100])
plt.show()

def runGraph(i):
    a1.appendleft(next(d))
    datatoplot = a1.pop()
    line.set_ydata(a1)
    plt.draw()
    plt.xlabel("Time Passed (Seconds)")
    plt.ylabel("Water Level (Meters)")
    plt.title("Dynamic Real Time Water Detection Disaster Preventer")
    # put a time stamp on all entries
    t = datetime.datetime.now().time()
    # writes entry plus a time stamp to the desired file
    file.write(str(t) + ":\t" + str(a1[0])+"m\n")
    i += 1
    time.sleep(0.01)
    plt.pause(0.000001)                

# write the results to a text file 
file = open("results.txt", "w")

i = 0

#run forever until the program is manually halted
while True:
    runGraph(i)
    i+=1
    
# close file and end program
file.close()
