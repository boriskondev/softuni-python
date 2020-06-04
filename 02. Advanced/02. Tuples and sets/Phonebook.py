phone_book = {}

while True:
    contact_info = input()
    if contact_info == "search":
        break
    contact, number = contact_info.split("-")
    phone_book[contact] = number

while True:
    search_name = input()
    if search_name == "stop":
        break
    if search_name in phone_book:
        print(f"{search_name} -> {phone_book[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
