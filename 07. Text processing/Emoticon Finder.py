text = input()

emoji = ""
emoticons = []

for i in range(len(text)):
    if text[i] == ":" and i+1 <= len(text):
        emoji = text[i] + text[i+1]
        emoticons.append(emoji)

[print(i) for i in emoticons]