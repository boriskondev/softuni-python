input_string = input().split(", ")

input_string.reverse()

if input_string[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for animal in input_string[0:]:
        if animal == "wolf":
            dead_sheep = input_string.index(animal)
            print(f"Oi! Sheep number {dead_sheep}! You are about to be eaten by a wolf!")