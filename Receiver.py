from __future__ import division
import numpy
from Point import Point
import numpy as np
import math

class Receiver:
    def __init__(self):
        self.h = numpy.array([[0, 0, 0, 1, 1, 1, 1],[0, 1, 1, 0, 0, 1, 1],[1, 0, 1, 0, 1, 0, 1],])
        self.regionPoints = {
            "1" : [Point(1/math.sqrt(10), 1/math.sqrt(10)), Point(1/math.sqrt(10), 3/math.sqrt(10)), Point(3/math.sqrt(10), 1/math.sqrt(10)), Point(3/math.sqrt(10), 3/math.sqrt(10))],
            "2" : [Point(1/math.sqrt(10), -1/math.sqrt(10)), Point(1/math.sqrt(10), -3/math.sqrt(10)), Point(3/math.sqrt(10), -1/math.sqrt(10)), Point(3/math.sqrt(10), -3/math.sqrt(10))],
            "3" : [Point(-1/math.sqrt(10), 1/math.sqrt(10)), Point(-1/math.sqrt(10), 3/math.sqrt(10)), Point(-3/math.sqrt(10), 1/math.sqrt(10)), Point(-3/math.sqrt(10), 3/math.sqrt(10))],
            "4" : [Point(-1/math.sqrt(10), -1/math.sqrt(10)), Point(-1/math.sqrt(10), -3/math.sqrt(10)), Point(-3/math.sqrt(10), -1/math.sqrt(10)), Point(-3/math.sqrt(10), -3/math.sqrt(10))]
        }
        
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
    
    def removeChannelImpact(self,point, hI, hQ):
        point.multiply(hI, -hQ)
        return point

    def demodulate16(self, point):
        if(point.getReal() > 0):
            if(point.getImaginary() > 0):
                nearestIdx = point.findNearest(self.regionPoints.get("1"))
                return("{0:b}".format(nearestIdx).zfill(4))
            else:
                nearestIdx = point.findNearest(self.regionPoints.get("4"))
                return("{0:b}".format(nearestIdx + 4).zfill(4))
        else :
            if(point.getImaginary() > 0):
                nearestIdx = point.findNearest(self.regionPoints.get("2"))
                return("{0:b}".format(nearestIdx + 8).zfill(4))
            else:
                nearestIdx = point.findNearest(self.regionPoints.get("3"))
                return("{0:b}".format(nearestIdx + 12).zfill(4))

    
    def decodeHamming(self, message):
        dec = numpy.dot(self.h, message)%2
        return dec
    



    
    

        

       
