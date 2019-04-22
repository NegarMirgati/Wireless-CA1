from __future__ import division
import numpy
from Point import Point
import numpy as np

class Receiver:
    def __init__(self):
        h = numpy.array([[0, 0, 0, 1, 1, 1, 1],[0, 1, 1, 0, 0, 1, 1],[1, 0, 1, 0, 1, 0, 1],])
        
    def demodulate2(self, point):
        if(point.getReal() > 0):
            if(point.getImaginary() > 0):
                return "11"
            else:
                return "10"
        else:
            if(point.getImaginary() > 0):
                return "01"
            else:
                return "00"
    
    def decodeHamming(self, message):
        dec = numpy.dot(self.h, message)%2
        return dec
    
    

        

       
