from tkinter import *

root = Tk()
root.configure(background="grey")
root.title("Calculator")
e = Entry(root, width=40, borderwidth=5, bg="grey", fg="yellow")
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


def buttonNum(number):
    # e.delete(0,END)
    current = e.get()  # gets the number currently in the input box and stores in current
    e.delete(0, END)  # deletes the number from input box
    global firstNum
    firstNum = str(current)+str(number)
    # if we put another number it forms a string with the old number that we put
    e.insert(0, firstNum)


def buttonC():
    e.delete(0, END)


def addition():
    firstNum = e.get()
    global fNum
    global math

    fNum = int(firstNum)
    math = "add"
    e.delete(0, END)


def subtraction():
    firstNum = e.get()
    global fNum
    global math

    fNum = int(firstNum)
    math = "sub"
    e.delete(0, END)


def multiplication():
    firstNum = e.get()
    global fNum
    global math

    fNum = int(firstNum)
    math = "mul"
    e.delete(0, END)


def division():
    firstNum = e.get()
    global fNum
    global math

    fNum = int(firstNum)
    math = "div"
    e.delete(0, END)


def power():
    firstNum = e.get()
    global fNum
    global math

    fNum = int(firstNum)
    math = "pow"

    e.delete(0, END)


def oneBy():
    firstNum = e.get()
    e.delete(0, END)
    global fNum
    global math

    fNum = int(firstNum)
    e.insert(0, f"1/{fNum}")
    math = "by"


def equation():
    secondNum = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, fNum + int(secondNum))
    elif math == "sub":
        e.insert(0, fNum-int(secondNum))
    elif math == "div":
        newNum = fNum/int(secondNum)
        inttNum = int(newNum)
        e.insert(0, inttNum)
    elif math == "mul":
        e.insert(0, fNum*int(secondNum))
    elif math == "pow":
        e.insert(0, fNum**int(secondNum))
    elif math == "by":
        e.insert(0, 1/int(fNum))


button1 = Button(root, padx=40, pady=20, text="1", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(1))
button2 = Button(root, padx=40, pady=20, text="2", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(2))
button3 = Button(root, padx=40, pady=20, text="3", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(3))
button4 = Button(root, padx=40, pady=20, text="4", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(4))
button5 = Button(root, padx=40, pady=20, text="5", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(5))
button6 = Button(root, padx=40, pady=20, text="6", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(6))
button7 = Button(root, padx=40, pady=20, text="7", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(7))
button8 = Button(root, padx=40, pady=20, text="8", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(8))
button9 = Button(root, padx=40, pady=20, text="9", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(9))
button0 = Button(root, padx=40, pady=20, text="0", fg="#FFBD35",
                 bg="black", command=lambda: buttonNum(0))

buttonClear = Button(root, padx=85, pady=20, text="Clear",
                     fg="#FFBD35", bg="black", command=buttonC)
buttonEqual = Button(root, padx=85, pady=20, text="=",
                     fg="#FFBD35", bg="black", command=equation)
buttonAdd = Button(root, padx=40, pady=20, text="+",
                   fg="#FFBD35", bg="black", command=addition)
buttonSub = Button(root, padx=40, pady=20, text="-",
                   fg="#FFBD35", bg="black", command=subtraction)
buttonDiv = Button(root, padx=40, pady=20, text="/",
                   fg="#FFBD35", bg="black", command=division)
buttonMul = Button(root, padx=40, pady=20, text="x",
                   fg="#FFBD35", bg="black", command=multiplication)
buttonPow = Button(root, padx=40, pady=20, text="^",
                   fg="#FFBD35", bg="black", command=power)
buttonBy = Button(root, padx=40, pady=20, text="1/x",
                  fg="#FFBD35", bg="black", command=oneBy)

button1.grid(row=3, column=0, sticky="nsew")
button2.grid(row=3, column=1, sticky="nsew")
button3.grid(row=3, column=2, sticky="nsew")

button4.grid(row=2, column=0, sticky="nsew")
button5.grid(row=2, column=1, sticky="nsew")
button6.grid(row=2, column=2, sticky="nsew")

button7.grid(row=1, column=0, sticky="nsew")
button8.grid(row=1, column=1, sticky="nsew")
button9.grid(row=1, column=2, sticky="nsew")

button0.grid(row=4, column=0, sticky="nsew")
buttonEqual.grid(row=4, column=1, columnspan=2, sticky="nsew")

buttonAdd.grid(row=1, column=4, sticky="nsew")
buttonSub.grid(row=2, column=4, sticky="nsew")
buttonDiv.grid(row=3, column=4, sticky="nsew")
buttonMul.grid(row=4, column=4, columnspan=2, sticky="nsew")
buttonPow.grid(row=5, column=4, sticky="nsew")
buttonBy.grid(row=5, column=2, sticky="nsew")

buttonClear.grid(row=5, column=0, columnspan=2, sticky="nsew")

root.mainloop()
