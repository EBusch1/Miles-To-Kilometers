from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
# window.minsize(width=300, height=300)
window.config(padx=15, pady=15)


def calc_click():
    km_is_label["text"] = round((int(mile_input.get()) * 1.61), 2)


equal_label = Label(text="Is equal to")
equal_label.grid(column=0, row=1)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

km_is_label = Label(text="0")
km_is_label.grid(column=1, row=1)

calc_button = Button(text="Calculate", command=calc_click)
calc_button.grid(column=1, row=2)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)

window.mainloop()
