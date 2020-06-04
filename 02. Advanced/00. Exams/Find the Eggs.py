def find_strongest_eggs(li, number_of_lists):
    strongs = []
    sub_lists = [[] for _ in range(number_of_lists)]
    for i, item in enumerate(li):
        sub_lists[i % number_of_lists].append(item)
    for sub_list in sub_lists:
        if len(sub_list) > 2:
            count = 0
            middle_index = int(len(sub_list) / 2)
            if sub_list[middle_index] > sub_list[middle_index - 1] and sub_list[middle_index] > sub_list[middle_index + 1]:
                left_side = sub_list[:middle_index]
                right_side = sub_list[middle_index+1:]
                if len(left_side) > len(right_side):
                    left_side = left_side[:len(right_side)]
                elif len(right_side) > len(left_side):
                    right_side = right_side[:len(left_side)]
                for a, b in zip(left_side, right_side):
                    if b > a:
                        count += 1
                if count == len(left_side):
                    strongs.append(sub_list[middle_index])
    return strongs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
