decrease = [int(x) for x in input().split()]

while True:
    counter = 0
    text = input()
    if text == "find":
        break
    text = list(text)
    for i in range(len(text)):
        if counter == len(decrease):
            counter = 0
        text[i] = chr(ord(text[i]) - decrease[counter])
        counter += 1
    text = ''.join(text)
    treasure_start = text.index("&") + 1
    treasure_end = text.index("&", treasure_start)
    coord_start = text.index("<") + 1
    coord_end = text.index(">", coord_start)
    treasure = text[treasure_start:treasure_end]
    coordinates = text[coord_start:coord_end]
    print(f"Found {treasure} at {coordinates}")