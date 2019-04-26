from __future__ import division
import numpy
from Point import Point
import math
import copy

class Transmitter:
    def __init__(self):
        '''generates [d1, d2, d3, d4, p1, p2, p3]'''
        self.g =  numpy.array([[1, 0, 0, 0, 1, 1, 0],[0, 1, 0, 0, 1, 0, 1],[0, 0, 1, 0, 0, 1, 1],[0, 0, 0, 1, 1, 1, 1]])
        self.qam16Dict = {
            "0000" : Point(1/math.sqrt(10), 1/math.sqrt(10)),
             "0001" : Point(1/math.sqrt(10), 3/math.sqrt(10)),
             "0010" : Point(3/math.sqrt(10), 1/math.sqrt(10)),
             "0011" :Point(3/math.sqrt(10), 3/math.sqrt(10)),
             "0100" :Point(1/math.sqrt(10), -1/math.sqrt(10)),
             "0101" :Point(1/math.sqrt(10), -3/math.sqrt(10)),
             "0110" :Point(3/math.sqrt(10), -1/math.sqrt(10)),
             "0111" :Point(3/math.sqrt(10), -3/math.sqrt(10)),
             "1000" :Point(-1/math.sqrt(10), 1/math.sqrt(10)),
             "1001" :Point(-1/math.sqrt(10), 3/math.sqrt(10)),
             "1010" :Point(-3/math.sqrt(10), 1/math.sqrt(10)),
             "1011" :Point(-3/math.sqrt(10), 3/math.sqrt(10)),
             "1100" :Point(-1/math.sqrt(10), -1/math.sqrt(10)),
             "1101" :Point(-1/math.sqrt(10), -3/math.sqrt(10)),
             "1110" :Point(-3/math.sqrt(10), -1/math.sqrt(10)),
             "1111" :Point(-3/math.sqrt(10), -3/math.sqrt(10))
        }

        
    def modulate(self, input):
        if(input == "00"):
            return Point(-0.707, -0.707)
        elif(input == "01"):
            return Point(-0.707, 0.707)
        elif(input == "10"):
            return Point(0.707, -0.707)
        else :
            return Point(0.707, 0.707)
    
    def modulate16QAM(self, input):
        return  copy.deepcopy(self.qam16Dict[input])

    
    def encodeHamming(self, message):
        enc = numpy.dot(message, self.g)%2
        return enc

