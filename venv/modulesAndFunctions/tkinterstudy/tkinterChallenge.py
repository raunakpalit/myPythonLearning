# Write a GUI program to create a simple calculator
# layout that looks like a screenshot
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("200x200")
mainWindow["padx"] = 10

# Define rows and columns
# mainWindow.columnconfigure(0, width=1)
# mainWindow.columnconfigure(1, width=1)
# mainWindow.columnconfigure(2, width=1)
# mainWindow.columnconfigure(3, width=1)
# mainWindow.columnconfigure(4, width=1)
# mainWindow.rowconfigure(0, width=1)
# mainWindow.rowconfigure(1, width=1)
# mainWindow.rowconfigure(2, width=1)
# mainWindow.rowconfigure(3, width=1)
# mainWindow.rowconfigure(4, width=1)
# mainWindow.rowconfigure(5, width=1)
# mainWindow.rowconfigure(6, width=1)

# Result space
resultSpace = tkinter.Entry(mainWindow)
resultSpace.grid(row=0, column=0, columnspan=4)

# Button Frame
cButton = tkinter.Button(mainWindow, text="C")
cButton.grid(row=1, column=0, sticky="nsew")
ceButton = tkinter.Button(mainWindow, text="CE")
ceButton.grid(row=1, column=1, sticky="nsew")
sevenButton = tkinter.Button(mainWindow, text="7")
sevenButton.grid(row=2, column=0, sticky="nsew")
fourButton = tkinter.Button(mainWindow, text="4")
fourButton.grid(row=3, column=0, sticky="nsew")
oneButton = tkinter.Button(mainWindow, text="1")
oneButton.grid(row=4, column=0, sticky="nsew")
eightButton = tkinter.Button(mainWindow, text="8")
eightButton.grid(row=2, column=1, sticky="nsew")
fiveButton = tkinter.Button(mainWindow, text="5")
fiveButton.grid(row=3, column=1, sticky="nsew")
twoButton = tkinter.Button(mainWindow, text="2")
twoButton.grid(row=4, column=1, sticky="nsew")
nineButton = tkinter.Button(mainWindow, text="9")
nineButton.grid(row=2, column=2, sticky="nsew")
sixButton = tkinter.Button(mainWindow, text="6")
sixButton.grid(row=3, column=2, sticky="nsew")
threeButton = tkinter.Button(mainWindow, text="3")
threeButton.grid(row=4, column=2, sticky="nsew")
plusButton = tkinter.Button(mainWindow, text="+")
plusButton.grid(row=2, column=3, sticky="nsew")
minusButton = tkinter.Button(mainWindow, text="-")
minusButton.grid(row=3, column=3, sticky="nsew")
multiplyButton = tkinter.Button(mainWindow, text="*")
multiplyButton.grid(row=4, column=3, sticky="nsew")
zeroButton = tkinter.Button(mainWindow, text="0")
zeroButton.grid(row=5, column=0, sticky="nsew")
equalButton = tkinter.Button(mainWindow, text="=")
equalButton.grid(row=5, column=1, sticky="nsew", columnspan=2)
divideButton = tkinter.Button(mainWindow, text="/")
divideButton.grid(row=5, column=3, sticky="nsew")

mainWindow.mainloop()