population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

fail = False

for person_wealth in range(len(population)):
    if population[person_wealth] >= minimum_wealth:
        continue
    else:
        difference = minimum_wealth - population[person_wealth]
        wealthiest = population.index(max(population))
        if population[wealthiest] > minimum_wealth:
            population[wealthiest] -= difference
            population[person_wealth] += difference
        else:
            print("No equal distribution possible")
            fail = True
            break

if not fail:
    print(population)