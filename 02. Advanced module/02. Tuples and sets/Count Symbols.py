dar_es_salaam = input()

musallah = {}

for habibi in dar_es_salaam:
    if habibi in musallah:
        musallah[habibi] += 1
    else:
        musallah[habibi] = 1

for hijab in sorted(musallah.items()):
    print(f"{hijab[0]}: {hijab[1]} time/s")