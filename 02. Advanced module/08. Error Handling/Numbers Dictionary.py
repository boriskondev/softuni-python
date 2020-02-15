# I solved the task in two different ways.
# The first one is according to the exercise - with one try and many except clauses.
# The second one (commented) is following the original code and it is a bit ugly,
# but I left it anyway as it was my initial solution.

# Solution 1

numbers_dictionary = {}

while True:
    line = input()
    try:
        if line == "End":
            break
        elif line == "Search":
            searched = input()
            if searched == "Remove":
                searched = input()
                if searched == "End":
                    break
                else:
                    del numbers_dictionary[searched]
            else:
                print(numbers_dictionary[searched])
        elif line == "Remove":
            searched = input()
            del numbers_dictionary[searched]
        else:
            number_as_string = line
            number = int(input())
            numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)

# Solution 2

'''
numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()

while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()

while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
'''