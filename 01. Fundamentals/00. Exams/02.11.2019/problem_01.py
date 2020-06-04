import math

biscuits_per_day_and_worker = int(input())
workers = int(input())
competing_factory_biscuits = int(input())

total_biscuits = 0
days_counter = 1

while days_counter < 31:
    if days_counter % 3 == 0:
        production = math.floor(0.75 * biscuits_per_day_and_worker * workers)
        total_biscuits += production
        days_counter += 1
        continue
    production = math.floor(biscuits_per_day_and_worker * workers)
    total_biscuits += production
    days_counter += 1

if total_biscuits > competing_factory_biscuits:
    difference = ((total_biscuits - competing_factory_biscuits) / competing_factory_biscuits) * 100
    print(f"You have produced {total_biscuits} biscuits for the past month.")
    print(f"You produce {difference:.2f} percent more biscuits.")
else:
    difference = ((competing_factory_biscuits - total_biscuits) / competing_factory_biscuits) * 100
    print(f"You have produced {total_biscuits} biscuits for the past month.")
    print(f"You produce {difference:.2f} percent less biscuits.")