to_remove = input()
whole_string = input()

while to_remove in whole_string:
    whole_string = whole_string.replace(to_remove, "")

print(whole_string)