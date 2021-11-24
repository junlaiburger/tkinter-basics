# Tkinter-basics
A study guide for learning the fundamentals of the python module tkinter

# Questions
1. What is tkinter?
2. What is Tcl/Tk?
3. 

# Cheat sheet
|Essential code|Description|
|:---:|:---:|
|from tkinter import * | import module|
|root = TK() |(first line) initialize tk interpreter|
|root.mainloop() |(last line) run event loop window| 

|Widget objects|Description|
|:---:|:---:|
|a = Entry() | creates an input field|
|b = Label() | creates a label|
|c = Button() | creates a button|

|Object methods|Description|
|:---:|:---:|
|a.get() | finds and returns a string|
|a.insert() | parameters (0, str/int)|
|a.delete() | parameters (0, END)|
|a.pack() | simple layout method, detailed method is "a.grid()"|
|a.grid() | parameters (row, column, columnspan, padx, pady)|

# Resources
1. Tkinter course by Codemy/John Elder - https://tinyurl.com/4tfd3fjv
2. Tkinter Python docs - https://docs.python.org/3/library/tk.html
3. Tcl - https://en.wikipedia.org/wiki/Tcl
