class Party:

    def __init__(self):
        self.people = []


party_1 = Party()
party_1.people.append("Pesho")
party_2 = Party()
party_2.people.append("Vili")

party_2.people.remove("Vili")

print(party_1.people)
print(party_2.people)