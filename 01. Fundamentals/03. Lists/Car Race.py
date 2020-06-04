race_track = list(map(int, input().split()))

left_time = 0
right_time = 0

for i in range(len(race_track) // 2):
    if race_track[i] == 0:
        left_time *= 0.8
    else:
        left_time += race_track[i]

race_track_rev = race_track[::-1]

for i in range(len(race_track_rev) // 2):
    if race_track_rev[i] == 0:
        right_time *= 0.8
    else:
        right_time += race_track_rev[i]

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")