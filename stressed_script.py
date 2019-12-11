from pathlib import Path
from docx import Document

MOST_WANTED = "ѝ"
times_found = 0

path_to_file = Path("C:/Users/pmg23_b.kondev/Desktop/Python/soft_uni/text.docx")

doc = Document(path_to_file)
paragraphs = doc.paragraphs

for paragraph in paragraphs:
    if MOST_WANTED in paragraph.text:
        times_found += len([word for word in paragraph.text.split() if MOST_WANTED in word])
        paragraph.text = paragraph.text.replace("ѝ", "HERE")
        # p.underline = True
        # p.bold = True

if times_found == 0:
    print("Не открих нищо!")
else:
    print(f"Открих  {times_found} ударени и-та!")

file_name = path_to_file.stem
doc.save(f"{file_name}_processed.docx")