from random import randint
import matplotlib.pyplot as plt
class Utils :
    def generate2BitData():
        f = open("input.txt", "w")
        for i in range(0, 10000):
            a0 = (randint(0, 1))
            a1 = (randint(0, 1))
            print >> f, (str(a0) + str(a1))
        
    def showScatterPlot(self, x, y):
        plt.scatter(x, y,  alpha=0.5)
        plt.title('Scatter plot pythonspot.com')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    
    def generate4BitData():
        f = open("input.txt", "w")
        for i in range(0, 10000):
            a0 = (randint(0, 1))
            a1 = (randint(0, 1))
            a2 = (randint(0, 1))
            a3 = (randint(0, 1))
            print >> f, (str(a0) + str(a1) + str(a2) + str(a3))
        


