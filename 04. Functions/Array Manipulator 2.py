def exchange(idx, numbers_list):
    if idx < 0 or idx > len(numbers_list):
        print("Invalid index")
    numbers_list = numbers_list[idx + 1:] + numbers_list[:idx + 1]
    return numbers_list


def max_idx(num_type, numbers_list):
    index_found = False
    max_number = -100000
    max_index = -1
    if num_type == "odd":
        for idx in range(len(numbers_list)):
            if numbers_list[idx] % 2 != 0:
                if numbers_list[idx] > max_number:
                    max_index = idx
                    max_number = numbers_list[idx]
                    index_found = True
    elif num_type == "even":
        for idx in range(len(numbers_list)):
            if numbers_list[idx] % 2 == 0:
                if numbers_list[idx] > max_number:
                    max_index = idx
                    max_number = numbers_list[idx]
                    index_found = True
    if not index_found:
        print("No matches")
    else:
        print(max_index)


def min_idx(num_type, numbers_list):
    index_found = False
    min_num = 100000
    min_index = -1
    if num_type == "odd":
        for idx in range(len(numbers_list)):
            if numbers_list[idx] % 2 != 0:
                if numbers_list[idx] <= min_num:
                    min_index = idx
                    min_num = numbers_list[idx]
                    index_found = True
    elif num_type == "even":
        for idx in range(len(numbers_list)):
            if numbers_list[idx] % 2 == 0:
                if numbers_list[idx] <= min_num:
                    min_index = idx
                    min_num = numbers_list[idx]
                    index_found = True
    if not index_found:
        print("No matches")
    else:
        print(min_index)


def first(count, num_type, numbers_list):
    if count > len(numbers_list):
        print("Invalid count")
    else:
        filtered_nums = []
        iterations = 0
        if num_type == "odd":
            for idx in range(len(numbers_list)):
                if numbers_list[idx] % 2 != 0:
                    filtered_nums.append(numbers_list[idx])
                    iterations += 1
                    if iterations == count:
                        break
        elif num_type == "even":
            for idx in range(len(numbers_list)):
                if numbers_list[idx] % 2 == 0:
                    filtered_nums.append(numbers_list[idx])
                    iterations += 1
                    if iterations == count:
                        break
        print(filtered_nums)


def last(count, num_type, numbers_list):
    if count > len(numbers_list):
        print("Invalid count")
    else:
        filtered_nums = []
        iterations = 0
        if num_type == "odd":
            for idx in range(len(numbers_list)-1, -1, -1):
                if numbers_list[idx] % 2 != 0:
                    filtered_nums.append(numbers_list[idx])
                    iterations += 1
                    if iterations == count:
                        break
        elif num_type == "even":
            for idx in range(len(numbers_list)-1, -1, -1):
                if numbers_list[idx] % 2 == 0:
                    filtered_nums.append(numbers_list[idx])
                    iterations += 1
                    if iterations == count:
                        break
        print(filtered_nums)


array = input().split()
array_length = len(array)
array = list(map(int, array))

while True:
    command = input().split()
    if command[0] == "end":
        break
    elif command[0] == "exchange":
        array = exchange(int(command[1]), array)
    elif command[0] == "max":
        max_idx(command[1], array)
    elif command[0] == "min":
        min_idx(command[1], array)
    elif command[0] == "first":
        first(int(command[1]), command[2], array)
    elif command[0] == "last":
        last(int(command[1]), command[2], array)

print(array)