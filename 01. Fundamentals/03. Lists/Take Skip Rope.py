input_string = input()

numbers = [int(x) for x in input_string if x.isnumeric()]
non_numbers = [x for x in input_string if not x.isnumeric()]

take_list = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
skip_list = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

take_skip_zipped = zip(take_list, skip_list)

decrypted_message = []

for take_skip in take_skip_zipped:
    decrypted_message.extend(non_numbers[:take_skip[0]])
    cut = take_skip[0] + take_skip[1]
    non_numbers = non_numbers[cut:]

print("".join(decrypted_message))