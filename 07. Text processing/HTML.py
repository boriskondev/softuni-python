title = input()
print(f"<h1>\n\t{title}\n</h1>")
article = input()
print(f"<article>\n\t{article}\n</article>")

while True:
    comment = input()
    if comment == "end of comments":
        break
    print(f"<div>\n\t{comment}\n</div>")