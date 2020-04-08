from collections import deque

formed_colors = []
main_colors = ["red", "yellow", "blue"]
keep_for_later = []

test = input().split()

queue = deque(test)

while queue:
    found = False
    if len(queue) > 1:
        first, last = queue[0], queue[-1]
        if first + last in main_colors:
            formed_colors.append(first+last)
            queue.popleft()
            queue.pop()
            found = True
        elif last + first in main_colors:
            formed_colors.append(last+first)
            queue.popleft()
            queue.pop()
            found = True
        elif first + last == "orange":
            if "red" in formed_colors and "yellow" in formed_colors:
                formed_colors.append(first + last)
                queue.popleft()
                queue.pop()
                found = True
            else:
                keep_for_later.append(first + last)
                formed_colors.append(first + last)
                queue.popleft()
                queue.pop()
                found = True
        elif last + first == "orange":
            if "red" in formed_colors and "yellow" in formed_colors:
                formed_colors.append(last + first)
                queue.popleft()
                queue.pop()
                found = True
            else:
                keep_for_later.append(last + first)
                formed_colors.append(last + first)
                queue.popleft()
                queue.pop()
                found = True
        elif first + last == "purple":
            if "red" in formed_colors and "blue" in formed_colors:
                formed_colors.append(first + last)
                queue.popleft()
                queue.pop()
                found = True
            else:
                keep_for_later.append(first + last)
                formed_colors.append(first + last)
                queue.popleft()
                queue.pop()
                found = True
        elif last + first == "purple":
            if "red" in formed_colors and "blue" in formed_colors:
                formed_colors.append(last + first)
                queue.popleft()
                queue.pop()
                found = True
            else:
                keep_for_later.append(last + first)
                formed_colors.append(last + first)
                queue.popleft()
                queue.pop()
                found = True
        elif first + last == "green":
            if "yellow" in formed_colors and "blue" in formed_colors:
                formed_colors.append(first + last)
                queue.popleft()
                queue.pop()
                found = True
            else:
                keep_for_later.append(first + last)
                formed_colors.append(first + last)
                queue.popleft()
                queue.pop()
                found = True
        elif last + first == "green":
            if "yellow" in formed_colors and "blue" in formed_colors:
                formed_colors.append(last + first)
                queue.popleft()
                queue.pop()
                found = True
            else:
                keep_for_later.append(last + first)
                formed_colors.append(last + first)
                queue.popleft()
                queue.pop()
                found = True
        if not found:
            first, last = first[:-1], last[:-1]
            formed_string = first + last
            queue.popleft()
            queue.pop()
            middle = int(len(queue) / 2)
            queue.insert(middle, formed_string.strip())
    else:
        if queue[-1] in main_colors:
            formed_colors.append(queue[-1])
            queue.pop()
        elif queue[-1] == "purple":
            if "red" in formed_colors and "blue" in formed_colors:
                formed_colors.append(queue[-1])
                queue.pop()
        else:
            break

for color in keep_for_later:
    if color == "orange":
        if "red" not in formed_colors or "yellow" not in formed_colors:
            formed_colors.remove("orange")
    elif color == "purple":
        if "red" not in formed_colors or "blue" not in formed_colors:
            formed_colors.remove("purple")
    elif color == "green":
        if "yellow" not in formed_colors or "blue" not in formed_colors:
            formed_colors.remove("green")

print(formed_colors)

