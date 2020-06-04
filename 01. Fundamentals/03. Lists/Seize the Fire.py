fire_and_needed_water = input().split("#")
water = int(input())

effort = 0
water_used = 0
watered_cells = []


for fire in fire_and_needed_water:
    fire_type, needed_water = fire.split(" = ")
    needed_water = int(needed_water)
    if needed_water <= water:
        if fire_type == "Low":
            if 1 <= needed_water <= 50:
                water -= needed_water
                water_used += needed_water
                effort += needed_water * 0.25
                watered_cells.append(needed_water)
        elif fire_type == "Medium":
            if 51 <= needed_water <= 80:
                water -= needed_water
                water_used += needed_water
                effort += needed_water * 0.25
                watered_cells.append(needed_water)
        elif fire_type == "High":
            if 81 <= needed_water <= 125:
                water -= needed_water
                water_used += needed_water
                effort += needed_water * 0.25
                watered_cells.append(needed_water)

print("Cells:")
for cell in watered_cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {water_used}")