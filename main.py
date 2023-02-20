import random
from personClass import person
from generationClass import generation
import matplotlib.pyplot as plt
people = [person(5, 5, True)]

for i in range(50):
    x = random.randint(-8, -5)
    y = random.randint(-8, -5)
    people.append(person(x, y, False))

def graph(gen, title):
    plt.figure()
    persons = gen.getPeople()
    for i in persons:
        xvalue = i.getCoordinates()[0]
        yvalue = i.getCoordinates()[1]
        chosen = i.getCoordinates()[3]
        if i.getCoordinates()[3]:
            plt.scatter(x = xvalue, y = yvalue, c = 'magenta', s = 10, linewidth = 0)
        else:
            plt.scatter(x = xvalue, y = yvalue, c = 'blue', s = 10, linewidth = 0)
            plt.title(title)
    plt.xlim([-20, 20])
    plt.ylim([-20, 20])

    plt.show()

generation1 = generation(people)
graph(generation1, "Generation 1")
generationToEvolve = generation1
for i in range(10):
    newGeneration = generation(generationToEvolve.evolve())
    graph(newGeneration, "Generation " + str(i + 2))
    generationToEvolve = newGeneration


    