class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result = f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {self.__animals}"
        return result


zoo_name = input()
lines = int(input())

zoo_obj = Zoo(zoo_name)

for line in range(lines):
    species, name = input().split()
    zoo_obj.add_animal(species, name)

show_animal = input()

print(zoo_obj.get_info(show_animal))