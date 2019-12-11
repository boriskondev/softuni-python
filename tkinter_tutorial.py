from tkinter import *
from tkinter import filedialog


def clicked():
    global filename
    filename = filedialog.askopenfile(filetypes=(("Word files","*.docx"),))


def file():
    f = filename.name
    return f


window = Tk()
window.geometry()
window.title("Stressed App")
open_file_label = Label(window, text="Open your docx file here:", font=("Arial", 10), padx=5, pady=5)
open_file_label.grid(column=0, row=0)
open_file_button = Button(window, text="Click me", command=clicked, padx=5, pady=5)
open_file_button.grid(column=1, row=0)

op = file()
print(op)

window.mainloop()