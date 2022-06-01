import tkinter as tk
import turtle
import random
import sys
from datetime import datetime


def randomize():
    """Randomizes"""
    random.seed(datetime.now())
    for turt in range(50):
        x = random.randint(0, 49)
        y = random.randint(0, 49)
        temp = 0
        temp2 = 0
        temp = turtList[x].xcor()
        temp2 = turtList[y].xcor()
        turtList[x].goto(temp2, -145)
        turtList[y].goto(temp, -145)
        sortArr[x], sortArr[y] = sortArr[y], sortArr[x]
        turtList[x], turtList[y] = turtList[y], turtList[x]


def exitprog():
    """exit case"""
    sys.exit()


def insertion():
    """insertion Sort"""
    #
    # Traverse through 1 to len(arr)
    for i in range(1, len(turtList)):
        key = sortArr[i]

        j = i - 1
        while j >= 0 and key < sortArr[j]:
            temp = turtList[j + 1].xcor()
            temp2 = turtList[j].xcor()
            turtList[j + 1].goto(temp2, -145)
            turtList[j].goto(temp, -145)
            sortArr[j], sortArr[j + 1] = sortArr[j + 1], sortArr[j]
            turtList[j], turtList[j + 1] = turtList[j + 1], turtList[j]
            j -= 1


def bubble():
    """Bubble Sort"""
    n = len(sortArr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if sortArr[j] > sortArr[j + 1]:
                # sleep(0.2)
                temp = turtList[j + 1].xcor()
                temp2 = turtList[j].xcor()
                turtList[j + 1].goto(temp2, -145)
                turtList[j].goto(temp, -145)
                sortArr[j], sortArr[j + 1] = sortArr[j + 1], sortArr[j]
                turtList[j], turtList[j + 1] = turtList[j + 1], turtList[j]


def selection():
    """Selection"""
    for i in range(len(sortArr)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(sortArr)):
            if sortArr[min_idx] > sortArr[j]:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        temp = turtList[i].xcor()
        temp2 = turtList[min_idx].xcor()
        turtList[i].goto(temp2, -145)
        turtList[min_idx].goto(temp, -145)
        sortArr[i], sortArr[min_idx] = sortArr[min_idx], sortArr[i]
        turtList[i], turtList[min_idx] = turtList[min_idx], turtList[i]


def check():
    """checks mode"""
    mode = v.get()
    if mode == 0:
        insertion()
    elif mode == 1:
        bubble()
    elif mode == 2:
        selection()

# Initial root
root = tk.Tk()
root.geometry('400x400')
root.title("Sorting Visualizer")
v = tk.IntVar()
v.set(0)

# List
l1 = tk.Label(root, text="The Sorting Visualizer")
l1.grid(row=11, column=5)
l3 = tk.Label(root, text="Sort Type")
l3.grid(row=3, column=11)

# Button
b1 = tk.Button(root, text="randomize", command=randomize)
b1.grid(row=12, column=5)
b2 = tk.Button(root, text="Go", command=check)
b2.grid(row=7, column=11)
b3 = tk.Button(root, text="Exit", command=exitprog)
b3.grid(row=12, column=11)

# Type of Operation
o1 = tk.Radiobutton(root, text="  Insertion", variable=v, value="0")
o2 = tk.Radiobutton(root, text="  Bubble", variable=v, value="1")
o3 = tk.Radiobutton(root, text="  Selection", variable=v, value="2")
o1.grid(row=4, column=11, sticky=tk.W)
o2.grid(row=5, column=11, sticky=tk.W)
o3.grid(row=6, column=11, sticky=tk.W)

# Turtle
canvas = tk.Canvas(master=root, width=300, height=300)

canvas.grid(row=1, column=1, columnspan=10, rowspan=10)
turtList = [turtle.RawTurtle(canvas) for i in range(50)]
for turt in range(50):
    turtList[turt].color("white")

sortArr = []

for turt in range(50):
    sortArr.append(turt)
    turtList[turt].ht()
    turtList[turt].speed(0)
    turtList[turt].pu()
    turtList[turt].setheading(90)
    turtList[turt].shape("square")
    turtList[turt].turtlesize(stretch_wid=(1 / 5), stretch_len=((int(turt) + 1) * .5), outline=None)
    turtList[turt].goto((turt * 6 - 145 / .95), (-145))
    turtList[turt].st()
    turtList[turt].color("black")
# Turtle Creation
# Mainloop

root.mainloop()