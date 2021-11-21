from tkinter import *

# Initialize tk interpreter
root = Tk()


def myClick():
	myLabel = Label(root, text="Look! I clicked a Button!!")
	myLabel.pack()

  
myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

# Starts the event loop of the window
root.mainloop()
