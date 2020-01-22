pairs = int(input())

longest_intersection = []

for pair in range(pairs):
    first_range, second_range = input().split("-")
    first_range_start, first_range_end = list(map(int, first_range.split(",")))
    second_range_start, second_range_end = list(map(int, second_range.split(",")))
    first_set = set([num for num in range(first_range_start, first_range_end+1)])
    second_set = set([num for num in range(second_range_start, second_range_end+1)])
    intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} " + f"with length {len(longest_intersection)}")
