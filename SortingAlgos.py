
import time
import sys

MAX_SIZE = sys.maxsize



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
############# Selection Sort #############

def selection_sort(data, drawData, timeTick):
    for z in range(len(data) - 1):
        small = z
        stall = data[z]
        for i in range(z + 1, len(data)):
            drawData(data, [('lightgreen' if x == small else ('lightblue' if x == i else '#3b4249')) for x in
                            range(len(data))])
            time.sleep(timeTick)
            if stall > data[i]:
                small = i
                stall = data[i]
        drawData(data,
                 [('lightgreen' if x == small else ('lightblue' if x == i else '#3b4249')) for x in range(len(data))])
        time.sleep(timeTick)
        temp = data[small]
        data[small] = data[z]
        data[z] = temp

    drawData(data, ['green' for x in range(len(data))])

def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)

    drawData('red' for stk in range(len(data)))
    time.sleep(timeTick)


def merge_sort_alg(data, start, end, drawData, timeTick):
    mid = (start + end) // 2
    if (start >= end):
        return
    if start < end:
        merge_sort_alg(data, start, mid, drawData, timeTick)
        merge_sort_alg(data, mid + 1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)


def merge(data, start, mid, end, drawData, timeTick):
    drawData(data, ['blue' for stk in range(len(data))])
    time.sleep(timeTick)

    arr = []
    i = start
    j = mid + 1
    k = start

    while i <= mid and j <= end:
        if data[i] < data[j]:
            arr[k] = data[i]
            i = i + 1;
            k = k + 1;
        else:
            arr[k] = data[j]
            j = j + 1
            k = k + 1

    if i <= mid:

        while i <= mid:
            arr[k] = data[i]
            i = i + 1;
            k = k + 1;
    elif j <= end:
        while j <= end:
            arr[k] = data[j];
            j = j + 1
            k = k + 1;

    data = arr

    drawData(data, ['lightblue' if x == i else '#3b4249' for x in range(len(data))])
    time.sleep(timeTick)
def partition(data, low, high, drawData, timeTick):
    i = (low - 1)
    pivot = data[high]
    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]

        for x in range(len(colordata)):
            if x == i:
                colordata[x] = '#ff0000'
            elif i < x < high:
                colordata[x] = 'lightyellow'
            elif x == high:
                colordata[x] = 'lightblue'
            else:
                colordata[x] = '#3b4249'

        drawData(data, colordata)
        time.sleep(timeTick)

    data[i + 1], data[high] = data[high], data[i + 1]
    return (i + 1)


def quickSort(data, low, high, drawData, timeTick):
    if low < high:
        pi = partition(data, low, high, drawData, timeTick)
        quickSort(data, low, pi - 1, drawData, timeTick)
        quickSort(data, pi + 1, high, drawData, timeTick)


def quick_sort(data, drawData, timeTick):
    global colordata
    colordata = ['#3b4249' for x in range(len(data))]
    quickSort(data, 0, len(data) - 1, drawData, timeTick)
    drawData(data, ['green' for x in range(len(data))])


############# Heap Sort #############
def merge_sort(data, drawData, timeTick):
    algo_merge(data, 0, len(data) - 1, drawData, timeTick)

    drawData(data, ['green' for x in range(len(data))])
    time.sleep(timeTick)


def algo_merge(data, left, right, drawData, timeTick):
    if left >= right:
        return
    middle = (left + right) // 2

    algo_merge(data, left, middle, drawData, timeTick)
    algo_merge(data, middle + 1, right, drawData, timeTick)
    merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, ['#3b4249' for x in range(len(data))])
    time.sleep(timeTick)

    leftside = data[left:middle + 1]
    rightside = data[middle + 1:right + 1]

    leftarr, rightarray = 0, 0

    for ink in range(left, right + 1):
        if leftarr < len(leftside) and rightarray < len(rightside):
            if leftside[leftarr] <= rightside[rightarray]:
                data[ink] = leftside[leftarr]
                leftarr += 1
            else:
                data[ink] = rightside[rightarray]
                rightarray += 1
        elif leftarr < len(leftside):
            data[ink] = leftside[leftarr]
            leftarr += 1
        else:
            data[ink] = rightside[rightarray]
            rightarray += 1

        drawData(data, ['lightblue' if x == ink else '#3b4249' for x in range(len(data))])
        time.sleep(timeTick)
colordata = []


def heap_sort(data, drawData, timeTick):
    global colordata
    colordata = ['#3b4249' for x in range(len(data))]

    n = len(data)

    for i in range(n):
        if data[i] > data[int((i - 1) / 2)]:
            j = i

            while data[j] > data[int((j - 1) / 2)]:
                data[j], data[int((j - 1) / 2)] = data[int((j - 1) / 2)], data[j]
                j = int((j - 1) / 2)

                drawData(data, ['lightblue' if x == i else colordata[x] for x in range(len(data))])
                time.sleep(timeTick)

    for i in range(n - 1, 0, -1):

        data[0], data[i] = data[i], data[0]

        j, index = 0, 0

        while True:
            index = 2 * j + 1

            if (index < (i - 1) and
                    data[index] < data[index + 1]):
                index += 1

            if index < i and data[j] < data[index]:
                data[j], data[index] = data[index], data[j]

            j = index

            drawData(data, ['lightyellow' if x == i or x == 0 else colordata[x] for x in range(len(data))])
            time.sleep(timeTick)
            if index >= i:
                break
    drawData(data, ['grey' for x in range(len(data))])
    time.sleep(timeTick)

