from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.6
    result.config(text=km)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


label = Label(text="is equal to")
label.grid(column=0, row=1)

result = Label(text=0)
result.grid(column=1, row=1)

mile_unit = Label(text="Miles")
mile_unit.grid(column=2, row=0)

km_unit = Label(text="Km")
km_unit.grid(column=2, row=1)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()

