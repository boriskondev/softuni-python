# not working properly and have to be amended for sure

from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

queue = deque()

cars_passed = 0
time_passed = 0
lights_off = False

while True:
    command = input()
    if lights_off:
        break
    if command == "END":
        break
    elif command == "green":
        time_passed = green_light_duration
        while queue:
            currently_passing = list(queue.popleft())
            if lights_off:
                break
            while currently_passing:
                currently_passing.pop(0)
                time_passed -= 1
                if time_passed == 0:
                    if free_window_duration >= len(currently_passing):
                        cars_passed += 1
                        lights_off = True
            cars_passed += 1
    else:
        queue.append(command)

if lights_off:
    print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")