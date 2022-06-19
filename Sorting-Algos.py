import time
import sys

MAX_SIZE = sys.maxsize

# Insertion Sort
def insertion_sort(data, drawData, timeTick):
    for i in range(1,len(data)): # Run the loop through the entireity of the Array
        value = data[i]
        j = i
        while value <= data[j-1] and j != 0:
        # While there exists a smaller element than current at a larger index keep swapping
            drawData(data, ['lightgreen' if x == j else '#3b4249' for x in range(len(data))])
            time.sleep(timeTick)

            data[j],data[j-1] = data[j-1],data[j]
            j -= 1

        drawData(data, ['lightgreen' if x == j else '#3b4249' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
    #Printing the sorted Array
