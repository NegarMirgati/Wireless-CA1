import numpy as np
from Point import Point

class WirelessChannel:
    def __init__(self, AWGNsigma):
        self.AWGNsigma = AWGNsigma
    
    def setSigma(self, val):
        self.AWGNsigma = val

    def applyChannelGain(self, point):
        hI =  np.random.normal(0, 1)
        hQ = np.random.normal(0, 1)
        point.multiply(hI * 0.707, hQ * 0.707)
        return(hI, hQ)

    def applyAWGN(self, point):
        nI = np.random.normal(0, self.AWGNsigma)
        nQ = np.random.normal(0, self.AWGNsigma)
        point.move(nI * 0.707, nQ * 0.707)

        

