from random import randint
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from Point import Point

class Utils :
    def generate2BitData(self):
        f = open("input.txt", "w")
        for i in range(0, 10000):
            a0 = (randint(0, 1))
            a1 = (randint(0, 1))
            print >> f, (str(a0) + str(a1))
        
    def showScatterPlot(self, predicted, SNR, color):
        fig, ax = plt.subplots()
        data1=[]
        data2= []
        for i in range(len(predicted)):
            data1.append(predicted[i].getReal())
            data2.append(predicted[i].getImaginary())

 
        r1 = Point(-0.707, -0.707)
        r2 = Point(-0.707, 0.707)
        r3 = Point(0.707, -0.707)
        r4 = Point(0.707, 0.707)

        ax.scatter(data1, data2, c = color)
        ax.scatter(r1.getReal(), r1.getImaginary() ,c = 'cyan')
        ax.scatter(r2.getReal(), r2.getImaginary() ,c = 'blue')
        ax.scatter(r3.getReal(), r3.getImaginary() ,c = 'green')
        ax.scatter(r4.getReal(), r4.getImaginary() ,c = 'red')

        ax.set_xlabel('I', fontsize=15)
        ax.set_ylabel('Q', fontsize=15)
        ax.set_title('Received signal for SNR= '+str(SNR))

        ax.grid(True)
        fig.tight_layout()
        plt.show()
    
    def generate4BitData(self):
        f = open("input.txt", "w")
        for i in range(0, 10000):
            a0 = (randint(0, 1))
            a1 = (randint(0, 1))
            a2 = (randint(0, 1))
            a3 = (randint(0, 1))
            print >> f, (str(a0) + str(a1) + str(a2) + str(a3))
    
    def probVsSNR(self, x, y):
        fig, ax = plt.subplots()
        ax.plot(x, y)

        ax.set(xlabel='SNR', ylabel='Probability',
        title='Probability VS SNR')
        ax.grid()

        fig.savefig("test.png")
        plt.show()




def main():
    u = Utils()
    u.generate2BitData()

if __name__ == "__main__":
    main()
        


