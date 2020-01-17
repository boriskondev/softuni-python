import re

regex = r"^(?P<start_end>[#$%*&])(?P<racer_name>[a-zA-Z]+)(?P=start_end)=(?P<code_length>\d+)!!(?P<code>.+$)"

while True:
    text = input()
    match = re.match(regex, text)
    if not match:
        print("Nothing found!")
    else:
        racer_name = match.group("racer_name")
        code_length = int(match.group("code_length"))
        code = match.group("code")
        if code_length != len(code):
            print("Nothing found!")
        else:
            code = ''.join([chr(ord(x) + code_length) for x in code])
            print(f"Coordinates found! {racer_name} -> {code}")
            exit(0)
    if not text:
        break