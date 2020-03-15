import random


class RandomList(list):
    def get_random_element(self):
        result = random.choice(self)
        return result


l = [1, 2, 3, 4]

li = RandomList(l)

print(li.get_random_element())