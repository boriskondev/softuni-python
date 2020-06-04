regular = []
vip = []

while True:
    reservation = input()
    if reservation == "PARTY":
        break
    if reservation[0].isdigit():
        vip.append(reservation)
    else:
        regular.append(reservation)

while True:
    who_came = input()
    if who_came == "END":
        break
    if who_came[0].isdigit():
        vip.remove(who_came)
    else:
        regular.remove(who_came)

print(len(regular) + len(vip))
[print(x) for x in sorted(vip)]
[print(x) for x in sorted(regular)]