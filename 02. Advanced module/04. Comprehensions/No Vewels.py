text = input()

vowels = ["a", "o", "u", "e", "i"]

processed_text = [char for char in text if char not in vowels]

print("".join(processed_text))