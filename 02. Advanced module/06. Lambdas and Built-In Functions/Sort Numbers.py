scrap = input().split()
print(" ".join(list(map(str, sorted([int(x) for x in scrap if x.isdigit() and int(x) > len(scrap)])))))