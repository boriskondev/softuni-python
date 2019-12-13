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

file_path = Path(chosen_file)

doc = Document(file_path)
paragraphs = doc.paragraphs

for paragraph in paragraphs:
    if MOST_WANTED in paragraph.text:
        times_found += len([word for word in paragraph.text.split() if MOST_WANTED in word])
        paragraph.text = paragraph.text.replace("ѝ", "|ѝ|")

if times_found == 0:
    messagebox.showinfo("Статус", "Не открих нищо!")
    quit(0)
elif times_found == 1:
    messagebox.showinfo("Статус", "Открито е едно ударено ѝ!\nВ същата папка ще откриеш нов файл с маркираното място.")
elif times_found > 1:
    messagebox.showinfo("Статус", f"Открити са {times_found} ударени ѝ-та!\nВ същата папка ще откриеш нов файл с маркираните места.")

file_folder = file_path.parent
file_name = file_path.stem
doc.save(f"{file_folder}/{file_name}_checked.docx")

application_window.mainloop()

# Име на скрипта - Удрѝ
# doc файлове дали чете?
# image of the program
# Работи ли на сървъра
# Как се прави exe - примера от Симеон
# program load, then a certain wait before everything
# a button OPEN?


# ЗА УТОЧНЯВАНЕ
# Да хваща и главна буква
# В името на файла - дали са намерени (и колко) или не, за да е ясно за дизайнерите.

# DONE
# Работи с файлове, именувани на български
# Запазва нов файл в директорията на избрания файл