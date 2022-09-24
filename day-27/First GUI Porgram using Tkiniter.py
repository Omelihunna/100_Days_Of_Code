from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"


#button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()





window.mainloop()
