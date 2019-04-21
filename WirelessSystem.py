from __future__ import division
from Transmitter import Transmitter
from  Receiver import Receiver
from WirelessChannel import WirelessChannel
from Utils import Utils

class WirelessSystem:
    def __init__(self, numOfInputs):
        self.transmitter = Transmitter()
        self.receiver = Receiver()
        self.wirelessChannel = WirelessChannel(0.1)
        self.numOfInputs = numOfInputs
        self.probabilites = []
        self.sigmaValues = [10, 1, 0.1]
    
    def run(self):
        for i in range(len(self.sigmaValues)):
            input = open("input.txt", "r")
            numOfCorrectOutputs = 0
            AWGNsigma = self.sigmaValues[i]
            print('for AWGNSgima =', AWGNsigma)
            self.wirelessChannel.setSigma(AWGNsigma)
            for line in input:
                data = line.rstrip()
                transmitterOut = self.transmitter.modulate(data)
                afterChannelGainApplied = self.wirelessChannel.applyChannelGain(transmitterOut)
                wirelessChannelOut = self.wirelessChannel.applyAWGN(afterChannelGainApplied)
                receiverOut = self.receiver.demodulate(wirelessChannelOut)
                if(data == receiverOut):
                    numOfCorrectOutputs += 1
            self.probabilites.append(numOfCorrectOutputs/self.numOfInputs)
            
            input.close()
        
        print('pppp', self.probabilites)
        


def main() :
    w = WirelessSystem(10000)
    w.run()

if __name__== "__main__":
      main()
        



        