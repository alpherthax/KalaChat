from tkinter import *


win = Tk()

win.title("KalaChat 0.0.0.ver")
win.geometry("1280x720")
Font = "MabinogiClassic 24 bold"
BGcolor = "#FFFAE3"

#baseframe

baseframe = Frame(win, bg=BGcolor)
baseframe.pack(fill=BOTH, expand=True)

lable = Label(baseframe, text="Hello, world!", font=Font, bg=BGcolor)
lable.pack(pady=15)


#charframe

chatframe = Frame(baseframe, bg=BGcolor)
chatframe.pack(fill=BOTH,expand=True, padx=240, pady=10)

#inputframe

inputframe = Frame(baseframe, bg=BGcolor)
inputframe.pack(expand= True, padx=240, pady=10)

button1 = Button(inputframe, text="+", relief="flat", bg="#ffb8ee", width=6, height=2)
button1.grid(row=0, column=0)

textbar = Entry(inputframe,text="Typing Text Here.", relief="flat", width=80)
textbar.grid(row=0,column=1)

button2 = Button(inputframe, text="send", relief="flat", bg="#ffb8ee", width=6, height=2)
button2.grid(row=0,column=2)


win.mainloop()