def data_types(data, string):
    result = ""
    if data == "int":
        result = int(string) * 2
    elif data == "real":
        result = f"{(float(string) * 1.5):.2f}"
    elif data == "string":
        result = "$" + string + "$"
    print(result)


data_type = input()
input_string = input()

data_types(data_type, input_string)