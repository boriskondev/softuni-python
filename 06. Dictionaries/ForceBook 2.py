force_book = {}

side = None
name = None

while True:
    input_string = input()
    if input_string == "Lumpawaroo":
        break
    if " | " in input_string:
        side, name = input_string.split(" | ")
        if side not in force_book:
            force_book[side] = []
        if name not in force_book[side]:
            force_book[side].append(name)
    elif " -> " in input_string:
        name, side = input_string.split(" -> ")
        if side not in force_book:
            force_book[side] = []
        for dict_side in force_book:
            if name in force_book[dict_side]:
                force_book[dict_side].remove(name)
                if len(force_book[dict_side]) == 0:
                    del force_book[dict_side]
                    break
        force_book[side].append(name)
        print(f"{name} joins the {side} side!" )

for side, names in sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(name) >= 1:
        print(f"Side: {side}, Members: {len(names)}")
        [print(f"! {name}") for name in sorted(names)]