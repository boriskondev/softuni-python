key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
legendary = False

while True:
    balastra = input().split()
    while len(balastra) > 0:
        quantity = int(balastra[0])
        material = balastra[1].lower()
        if material == "shards" or material == "fragments" or material == "motes":
            key_materials[material] += quantity
            if key_materials["shards"] >= 250:
                key_materials["shards"] -= 250
                print("Shadowmourne obtained!")
                legendary = True
                break
            elif key_materials["fragments"] >= 250:
                key_materials["fragments"] -= 250
                print("Valanyr obtained!")
                legendary = True
                break
            elif key_materials["motes"] >= 250:
                key_materials["motes"] -= 250
                print("Dragonwrath obtained!")
                legendary = True
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity
        balastra = balastra[2:]
    if legendary:
        break

for item, quantity in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{item}: {quantity}")
for item, quantity in sorted(junk.items(), key=lambda x: x[0]):
    print(f"{item}: {quantity}")