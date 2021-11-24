# Tkinter-basics
A study guide for learning the fundamentals of the python module tkinter

# Questions
1. What is tkinter?
2. What is Tcl/Tk?
3. 

# Cheat sheet
Essential
1. from tkinter import *      ## import module
2. root = TK()                ## initialize tk interpreter
3. root.mainloop()            ## run event loop window 

Widget objects
1. a = Entry()                ## creates an input field
2. b = Label()                ## creates a label
3. c = Button()               ## creates a button

Object methods
1. a.get()                    ## finds and returns a string
2. a.insert()                 ## parameters 0, str/int
3. a.delete()                 ## parameters 0, END
4. a.pack()                   ## simple layout method
5. a.grid()                   ## detailed layout method | parameters row, column, columnspan, padx, pady

# Resources
1. Tkinter course by Codemy/John Elder - https://tinyurl.com/4tfd3fjv
2. Tkinter Python docs - https://docs.python.org/3/library/tk.html
3. Tcl - https://en.wikipedia.org/wiki/Tcl
