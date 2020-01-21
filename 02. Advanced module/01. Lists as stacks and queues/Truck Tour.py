from collections import deque

gas_stations = int(input())

queue = deque()

for _ in range(gas_stations):
    fuel, kilometers = list(map(int, input().split()))
    station = fuel, kilometers
    queue.append(station)

current_station = 0
stations_passed = 0
current_fuel = 0

while True:
    fuel, kilometers = queue.popleft()
    station = fuel, kilometers
    current_fuel += fuel
    if current_fuel >= kilometers:
        current_fuel -= kilometers
        queue.append(station)
        stations_passed += 1
        if stations_passed == len(queue):
            print(current_station)
            break
    else:
        queue.append(station)
        current_station += 1
        current_fuel = 0
        if current_station > len(queue) - 1:
            break