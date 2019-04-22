import numpy
from Point import Point

class Transmitter:
    def __init__(self):
        self.g =  numpy.array([[1, 0, 0, 0, 0, 1, 1],[0, 1, 0, 0, 1, 0, 1],[0, 0, 1, 0, 1, 1, 0],[0, 0, 0, 1, 1, 1, 1]])

    def modulate(self, input):
        if(input == "00"):
            return Point(-0.707, -0.707)
        elif(input == "01"):
            return Point(-0.707, 0.707)
        elif(input == "10"):
            return Point(0.707, -0.707)
        else :
            return Point(0.707, 0.707)
    
    def encodeHamming(self, message):
        enc = numpy.dot(message, self.g)%2
        return enc

