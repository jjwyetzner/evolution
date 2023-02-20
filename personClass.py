import math
import random

class person:
    def __init__(self, x, y, chosenOne):
        self.x = x
        self.y = y
        self.chosenOne = chosenOne

    def getCoordinates(self):
        distance = math.sqrt(math.pow((10 - self.x), 2) + math.pow((10 - self.y), 2))
        return [self.x, self.y, distance, self.chosenOne]
    
    def getChosenOne(self):
        return self.chosenOne

    def reproduce(self, mate):
        weightingX = random.randint(1, 10) / 10
        randomnessX = random.randint(0, 2)
        weightingY = random.randint(1, 10) / 10
        randomnessY = random.randint(0, 2)

        newX = self.x * weightingX + (1 - weightingX) * mate.getCoordinates()[0] + randomnessX
        newY = self.y * weightingY + (1 - weightingY) * mate.getCoordinates()[1] + randomnessY
        isChosenOne = self.chosenOne or mate.getChosenOne()

        return person(newX, newY, isChosenOne)

