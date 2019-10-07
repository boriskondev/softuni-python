event_input = input()

events_low = ["coding", "cat", "dog", "movie"]
events_high = ["CODING", "CAT", "DOG", "MOVIE"]

sleep = 0

while event_input != "END":
    if event_input in events_low:
        sleep += 1
    elif event_input in events_high:
        sleep += 2
    event_input = input()

if sleep > 5:
    print("You need extra sleep")
else:
    print(sleep)