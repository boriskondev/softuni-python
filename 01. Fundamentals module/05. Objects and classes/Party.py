class Party:

    def __init__(self):
        self.people = []


party = Party()

guest = input()

while guest != "End":
    party.people.append(guest)
    guest = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")