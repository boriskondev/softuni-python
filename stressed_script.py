from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from docx import Document

MOST_WANTED = "ѝ"
times_found = 0

application_window = Tk()

chosen_file = filedialog.askopenfilename(parent=application_window, title="Please select a file:",
                                         filetypes=(("Word files", "*.docx"),))

path_to_file = Path(chosen_file)

doc = Document(path_to_file)
paragraphs = doc.paragraphs

for paragraph in paragraphs:
    if MOST_WANTED in paragraph.text:
        times_found += len([word for word in paragraph.text.split() if MOST_WANTED in word])
        paragraph.text = paragraph.text.replace("ѝ", "HERE")

if times_found == 0:
    messagebox.showinfo("Статус", "Не открих нищо!")
else:
    messagebox.showinfo("Статус", f"Открити са {times_found} ударени и-та!"
                                  f"\nВ същата папка ще откриеш нов файл с маркираните места.")
    file_name = path_to_file.stem
    doc.save(f"{file_name}_processed.docx")

# check if found = 1
# image of the program
# program load, then a certain wait before everything
# a button OPEN?
# to save the file in the location where the original one is

