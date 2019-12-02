current_list = list(map(int, input("Sequence: ").split()))
rows_to_display = int(input("Rows to display: "))

iterations = 0
number_counter = 1

while rows_to_display > iterations:
    new_list = []
    if len(current_list) == 1:
        new_list.append(number_counter)
        new_list.append(current_list[0])
    else:
        for index in range(0, len(current_list)):
            if index < (len(current_list) - 1):
                if current_list[index] == current_list[index + 1]:
                    number_counter += 1
                    continue
                else:
                    new_list.append(number_counter)
                    new_list.append(current_list[index])
                    number_counter = 1
            else:
                new_list.append(number_counter)
                new_list.append(current_list[index])
                number_counter = 1
    print(" ".join(map(str, new_list)))
    #[print(f"{count} -> {number},", end=" ") for count, number in zip(new_list[0::2], new_list[1::2])]
    #print()
    current_list = new_list
    del new_list
    iterations += 1