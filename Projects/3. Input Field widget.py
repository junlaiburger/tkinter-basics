from tkinter import *

root = Tk()

e = Entry(root, width=50, font=('Helvetica', 24))
e.pack()
e.insert(0, "Enter Your Name: ")


def my_click():
	hello = "Hello " + e.get()
	my_label = Label(root, text=hello)
	e.delete(0, 'end')
	my_label.pack()

  
my_button = Button(root, text="Enter Your Name", command=myClick)
my_button.pack()

root.mainloop()
