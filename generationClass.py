import random
from personClass import person

class generation:
    def __init__(self, people):
        self.people = people

    def getPeople(self):
        return self.people

    def evolve(self):
        # peopleCoordinates = []
        # for individual in self.people:
        #     peopleCoordinates.append(individual.getCoordinates())
        self.people.sort(key = lambda x: x.getCoordinates()[2])
        newGeneration = []
        newGenerationStats = []
        for i in range(round(len(self.people) * 0.25)):
        # for i in range(len(self.people)):
            whichMate = random.randint(1, 3)
            for j in range(random.randint(2,6)):
                newGeneration.append(self.people[0].reproduce(self.people[whichMate]))
                newGenerationStats.append(self.people[0].reproduce(self.people[whichMate]).getCoordinates())

            del self.people[whichMate]
            del self.people[0]

        print(newGenerationStats)
        return newGeneration
            
