while True:
    input_string = input()
    if input_string == "end":
        break
    print(f"{input_string} = {input_string[::-1]}")