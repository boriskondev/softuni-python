def read_file(list_to_process):
    for index in range(len(list_to_process)):
        if isinstance(list_to_process[index], list):
            read_file(list_to_process[index])
        elif isinstance(list_to_process[index], str):
            if list_to_process[index]:
                print(list_to_process[index])
    return list_to_process
