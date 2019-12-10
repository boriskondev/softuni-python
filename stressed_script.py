from docx import Document

doc = Document("text.docx")

for p in doc.paragraphs:
    paragraph_text = p.runs
    for p in paragraph_text:
        if "ѝ" in p.text:
            p.text = p.text.replace("ѝ", "HERE")
            print(p.text)

doc.save('demo.docx')
