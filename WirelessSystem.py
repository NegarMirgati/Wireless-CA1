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
        self.reveivedPoints = []
        self.colors = ['purple', 'yellow', 'orange']
    
    def runForScatterPlot(self):
        u = Utils() 
        for i in range(len(self.sigmaValues)):
            self.reveivedPoints = []
            input = open("input.txt", "r")
            numOfCorrectOutputs = 0
            AWGNsigma = self.sigmaValues[i]
            self.wirelessChannel.setSigma(1/AWGNsigma)
            for line in input:
                data = line.rstrip()
                transmitterOut = self.transmitter.modulate(data)
                afterChannelGainApplied = self.wirelessChannel.applyChannelGain(transmitterOut)
                wirelessChannelOut = self.wirelessChannel.applyAWGN(afterChannelGainApplied)
                self.reveivedPoints.append(wirelessChannelOut)
                receiverOut = self.receiver.demodulate2(wirelessChannelOut)
                if(data == receiverOut):
                    numOfCorrectOutputs += 1
            self.probabilites.append(1 - (numOfCorrectOutputs/self.numOfInputs))

            u.showScatterPlot(self.reveivedPoints ,AWGNsigma, self.colors[i])
            input.close()

        print('pppp', self.probabilites)
               
    def runForLinePlot(self):
        u = Utils() 
        for i in range(1, 100, 1):
            input = open("input.txt", "r")
            numOfCorrectOutputs = 0
            AWGNsigma = i / 10.0
            print('for AWGNSgima =', AWGNsigma)
            self.wirelessChannel.setSigma(1/AWGNsigma)
            for line in input:
                data = line.rstrip()
                transmitterOut = self.transmitter.modulate(data)
                afterChannelGainApplied = self.wirelessChannel.applyChannelGain(transmitterOut)
                wirelessChannelOut = self.wirelessChannel.applyAWGN(afterChannelGainApplied)
                receiverOut = self.receiver.demodulate2(wirelessChannelOut)
                if(data == receiverOut):
                    numOfCorrectOutputs += 1
            self.probabilites.append(1 - (numOfCorrectOutputs/self.numOfInputs))
            input.close()
        print('pppp', self.probabilites)
        u = Utils()
        u.probVsSNR([i/10.0 for i in range(1, 100, 1)], self.probabilites)
    


def main() :
    w = WirelessSystem(10000)
    w.runForLinePlot()
    w.runForScatterPlot()

if __name__== "__main__":
      main()
        



        