bands = {}


while True:
    event = input().split("; ")
    if event[0] == "start of concert":
        break
    elif event[0] == "Add":
        band_name = event[1]
        members = event[2].split(", ")
        if band_name not in bands:
            bands[band_name] = [0, []]
            bands[band_name][1] += members
        else:
            for member in members:
                if member not in bands[band_name][1]:
                    bands[band_name][1].append(member)
    elif event[0] == "Play":
        band_name = event[1]
        time_played = int(event[2])
        if band_name not in bands:
            bands[band_name] = [time_played, []]
        else:
            bands[band_name][0] += time_played

total_time = sum([bands[k][0] for k in bands])
print(f"Total time: {total_time}")
for band, info in sorted(bands.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{band} -> {info[0]}")

band_to_show = input()
print(band_to_show)
for band in bands:
    if band == band_to_show:
        for member in bands[band][1]:
            print(f"=> {member}")