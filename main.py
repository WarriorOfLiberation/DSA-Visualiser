
from tkinter import *
from tkinter import ttk
import random
from SortingAlgos import *
from tkinter import messagebox


HEIGHT = 500
WIDTH = 700

root = Tk()
root.title('Algorithm Visualization')

# Variables
selected_algo = StringVar()
data = []
exitFlag = False


# Functions
def drawData(data, colorArray):
    mainFrame.delete('all')
    #mainFrame.config(text="No. of comparisons: 0")
    heighh = mainFrame.winfo_height() - 10
    widtt = mainFrame.winfo_width()
    x_width = widtt / (len(data) + 1)
    offset = (widtt) / (len(data) * 10)
    spacing = 10
    #mainFrame.create_rectangle()
    for i, height in enumerate(data):
        # Top Left
        x0 = i * x_width + offset + spacing
        y0 = heighh - height * (heighh - 30)

        # Bottom Right
        x1 = (i + 1) * x_width + offset
        y1 = heighh

        mainFrame.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    #mainFrame.create_text('Time Complexity')
    root.update()


def makearray():
    global data

    # minVal = int(minEntry.get())
    # maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = [i for i in range(1, size)]
    # data = [random.randint(minVal, maxVal) for i in range(1,size)] # For generating data in given range
    random.shuffle(data)

    # Normalizing data
    data = [i / max(data) for i in data]

    drawData(data, ['#3b4249' for _ in range(len(data))])


def startAlgorithm():
    global data

    if data == sorted(data):
        return

    # Disabling Once ALgo is Started
    start_button['state'] = 'disabled'
    make_the_array_button['state'] = 'disabled'

    algorithm = ('_').join(algMenu.get().lower().split())
    print(algorithm)



    eval(algorithm + '(data, drawData, speedScale.get())')


    # Enabling the Button again

    start_button['state'] = 'normal'
    make_the_array_button['state'] = 'normal'

    # mainFrame.create_text(
    #       200, 100,
    #       fill="darkblue",
    #       font="Times 20 italic bold",
    #       text="with great power comes \ngreat responsibility")
    if (algorithm == 'selection_sort'):

        mainFrame.create_text(200, 100,
                              fill="darkblue",
                              font="Times 20 italic bold",
                              text="Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n²)")
    elif (algorithm == 'bubble_sort'):
        mainFrame.create_text(200, 100,
                              fill="darkblue",
                              font="Times 20 italic bold",
                              text="Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n)")
    elif (algorithm == 'heap_sort'):
        mainFrame.create_text(200, 100,
                              fill="darkblue",
                              font="Times 20 italic bold",
                              text="Worst Case:O(n*logn)\nAverage Case:O(n*logn)\nBest Case:O(n*logn)")
    elif (algorithm == 'merge_sort'):
        mainFrame.create_text(200, 100,
                              fill="darkblue",
                              font="Times 20 italic bold",
                              text="Worst Case:O(n*logn)\nAverage Case:O(n*logn)\nBest Case:O(n*logn)")
    elif (algorithm == 'quick_sort'):
        mainFrame.create_text(200, 100,
                              fill="darkblue",
                              font="Times 20 italic bold",
                              text="Worst Case:O(n^2)\nAverage Case:O(n*logn)\nBest Case:O(n*logn)")
    elif (algorithm == 'insertion_sort'):
        mainFrame.create_text(200, 100,
                              fill="darkblue",
                              font="Times 20 italic bold",
                              text="Worst Case:O(n^2)\nAverage Case:O(n^2)\nBest Case:O(n)")








canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
#canvas.config(text="No. of comparisons: 0")
format = Frame(root, width=WIDTH, height=HEIGHT, bg='pink', bd=15)
format.place(relx=0.5, rely=0, relwidth=0.96, relheight=0.3, anchor='n')
maxEntry = Scale(format, from_=10, to=100, resolution=1, orient=HORIZONTAL, label='Max Value', font=('Courier', 12))
maxEntry.place(relx=0.6, rely=0.53, relheight=0.47, relwidth=0.25)

# Generate Button
make_the_array_button = Button(format, text="Generate", command=makearray, bg='#ff80ed', fg='#133337', font=('courier', 10))
make_the_array_button.place(relx=0.87, rely=0.6, relwidth=0.13, relheight=0.3)


# Menu Row [1]
Label(format, text='Algorithm', bg='#f5f5dc', font=('Algerian', 25)).place(x=10, y=-9)

# Algorithm Selection Dropdown
algMenu = ttk.Combobox(format, textvariable=selected_algo,
                       values=['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort',
                               'Heap Sort'], font=('Aerial', 17))
algMenu.place(x=7, y=35, relheight=0.2, relwidth=0.4)
algMenu.current(0)


speedScale = Scale(format, from_=0.2, to=0.0, length=200, digits=2, resolution=0.0, orient=HORIZONTAL,
                   label='Select Speed [sec]', font=('Calibri', 12), bg='#ffd700')
speedScale.place(relx=0.45, rely=-0.07, relheight=0.5, relwidth=0.36)



# Menu Row[2] (Entry Scales)
sizeEntry = Scale(format, from_=10, to=150, resolution=1, orient=HORIZONTAL, label='Data Size', font=('Arial', 12), bg='#bada55')
sizeEntry.place(relx=0, rely=0.53, relheight=0.47, relwidth=0.25)

minEntry = Scale(format, from_=0, to=10, resolution=1, orient=HORIZONTAL, label='Min Value', font=('Arial', 12), bg='#7fffd5')
minEntry.place(relx=0.30, rely=0.53, relheight=0.47, relwidth=0.27)

# Start Button
start_button = Button(format, text="Start", command=startAlgorithm, bg='#ffc0cb', font=('Courier', 10))
start_button.place(relx=0.87, rely=0.1, relwidth=0.13, relheight=0.3)

mainFrame = Canvas(root, bg='#c6e2ff')
mainFrame.place(relx=0.5, rely=0.31, relwidth=1, relheight=0.68, anchor='n')



def on_closing():
    global exitFlag
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

