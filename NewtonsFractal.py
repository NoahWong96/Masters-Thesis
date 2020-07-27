import numpy.matlib
import numpy as np
import math
import sys


class NewtonsFractal:


    def __init__(self, a = 0, b = 0, dx = 0, dy = 0, rangex = 0, rangey = 0):

        self.a = a
        self.b = b
        self.dx = dx
        self.dy = dy
        self.rangex = rangex
        self.rangey = rangey

        self.distanceX = self.rangex[1] - self.rangex[0]
        self.distanceY = self.rangey[1] - self.rangey[0]

        self.dataPointsX = int(math.ceil(self.distanceX/self.dx))
        self.dataPointsY = int(math.ceil(self.distanceY/self.dy))

        self.dataPoints = self.dataPointsX * self.dataPointsY

        self.iterArray = np.matlib.ones((self.dataPoints, 4))

        self.numSolutions = 0
        self.solutions = 0

    def getParameter(self):
        return self.a,self.b

    def setParameter(self, a,b):
        self.a = a
        self.b = b

    def getRange(self):
        return self.rangex, self.rangey

    def setRange(self,rangex, rangey):
        this.rangex = rangex
        this.rangey = rangey

    def getdx(self):
        return self.dx



    def setIterArray(self):

        count = 0
        for i in range(0, self.dataPointsX):
            for j in range(0, self.dataPointsY):
                xValue = self.rangex[0] + (i * self.dx)
                yValue = self.rangey[0] + (j * self.dy)
                self.iterArray[count] = [xValue ,yValue , -1,-1 ]
                count=count+1

    def printIterArray(self):

        count = 0
        for i in range(0, self.dataPointsX):
            for j in range(0, self.dataPointsY):
                print(self.iterArray[count]),
                count = count + 1
            print()
        return

    def setSolutions(self):

        if self.b == 0:
            if np.absolute(self.a) < (2*math.sqrt(3)/3):
                self.numSolutions = 2
                self.solutions = np.matlib.ones((self.numSolutions,2))
                print(np.sqrt(((self.a*self.a )/4.0)+1))
                self.solutions[0] = [-1.0*(self.a/2.0) - math.sqrt(((self.a*self.a )/4.0)+1),0]
                self.solutions[1] = [-1.0*(self.a/2.0) + math.sqrt(((self.a*self.a )/4.0)+1),0]
            else:
                self.numSolutions = 4
                self.solutions = np.matlib.ones((self.numSolutions,2))
                self.solutions[0] = [-1.0*(self.a/2.0)- math.sqrt(((self.a*self.a )/4.0)+1),0]
                self.solutions[1] = [-1.0*(self.a/2.0)+ math.sqrt(((self.a*self.a )/4.0)+1),0]
                self.solutions[2] = [self.a/(-2.0), -(1/2.0)* math.sqrt(-4 + 3*self.a*self.a)]
                self.solutions[3] = [self.a/(-2.0), (1/2.0)* math.sqrt(-4 + 3*self.a*self.a)]
        #TODO: set solutions for when a = 0
        elif self.a == 0:
            print("todo")
        #else

    def printSolutions(self):
        for i in range(0, self.numSolutions):
            print(self.solutions[i])
        return


if __name__ == '__main__':
    image1 = NewtonsFractal(2,0,1,1,[-5,5],[-5,5])
    print(image1.getParameter())
    image1.setIterArray()
    #image1.printIterArray()
    image1.setSolutions()
    image1.printSolutions()



def iterFunction(a,b,x,y):
    numeratorX = a * (1 + x^2 - y^2) - 2*x*(1- b*y + x^2 + y^2)
    numeratorY = b * (1 + x^2 - y^2) - 2*y*(-1+a*x + x^2 + y^2)
    denominator = a^2 + b^2 - 4*(x^2 + y^2)

    if denominator ==0:
        return "infty"

    else:
        return [numeratorX/denominator, numeratorY/denominator]
