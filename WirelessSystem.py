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
        self.sigmaValues = [10, 1, 0.1]
        self.reveivedPoints = []
        self.colors = ['purple', 'yellow', 'orange']
    
    def runForScatterPlot(self):
        u = Utils() 
        probabilities = []
        for i in range(len(self.sigmaValues)):
            self.reveivedPoints = []
            input = open("input.txt", "r")
            numOfCorrectOutputs = 0
            AWGNsigma = self.sigmaValues[i]
            self.wirelessChannel.setSigma(1/AWGNsigma)
            for line in input:
                data = line.rstrip()
                transmitterOut = self.transmitter.modulate(data)
                (afterChannelGainApplied, hI, hQ) = self.wirelessChannel.applyChannelGain(transmitterOut)
                wirelessChannelOut = self.wirelessChannel.applyAWGN(afterChannelGainApplied)
                self.reveivedPoints.append(wirelessChannelOut)

            u.showScatterPlot(self.reveivedPoints ,AWGNsigma, self.colors[i])
            input.close()


    def runForScatterPlot16(self):
        u = Utils() 
        probabilities = []
        for i in range(len(self.sigmaValues)):
            self.reveivedPoints = []
            input = open("input4.txt", "r")
            numOfCorrectOutputs = 0
            AWGNsigma = self.sigmaValues[i]
            self.wirelessChannel.setSigma(1/AWGNsigma)
            for line in input:
                data = line.rstrip()
                transmitterOut = self.transmitter.modulate16QAM(data)
                (afterChannelGainApplied, hI, hQ) = self.wirelessChannel.applyChannelGain(transmitterOut)
                wirelessChannelOut = self.wirelessChannel.applyAWGN(afterChannelGainApplied)
                self.reveivedPoints.append(wirelessChannelOut)

            u.showScatterPlotQAM(self.reveivedPoints ,AWGNsigma, self.colors[i])
            input.close()
               
    def runForLinePlot(self):
        u = Utils() 
        probabilities = []
        for i in range(1, 100, 1):
            input = open("input.txt", "r")
            numOfCorrectOutputs = 0
            AWGNsigma = i / 10.0
            print('for AWGNSgima =', AWGNsigma)
            self.wirelessChannel.setSigma(1/AWGNsigma)
            for line in input:
                data = line.rstrip()
                transmitterOut = self.transmitter.modulate(data)
                (afterChannelGainApplied, hI, hQ) = self.wirelessChannel.applyChannelGain(transmitterOut)
                wirelessChannelOut = self.wirelessChannel.applyAWGN(afterChannelGainApplied)
                afterRemoval = self.receiver.removeChannelImpact(wirelessChannelOut, hI, hQ)
                receiverOut = self.receiver.demodulate2(afterRemoval)
                if(data == receiverOut):
                    numOfCorrectOutputs += 1
            probabilities.append(1 - (numOfCorrectOutputs/self.numOfInputs))
            input.close()
        u = Utils()
        u.probVsSNR([i/10.0 for i in range(1, 100, 1)], probabilities)


    def runForLinePlot16(self):
        u = Utils() 
        probabilities = []
        for i in range(1, 100, 1):
            input = open("input4.txt", "r")
            numOfCorrectOutputs = 0
            AWGNsigma = i / 10.0
            print('for AWGNSgima =', AWGNsigma)
            self.wirelessChannel.setSigma(1/AWGNsigma)
            for line in input:
                data = line.rstrip()
                transmitterOut = self.transmitter.modulate16QAM(data)
                (afterChannelGainApplied, hI, hQ) = self.wirelessChannel.applyChannelGain(transmitterOut)
                wirelessChannelOut = self.wirelessChannel.applyAWGN(afterChannelGainApplied)
                afterRemoval = self.receiver.removeChannelImpact(wirelessChannelOut, hI, hQ)
                receiverOut = self.receiver.demodulate16(afterRemoval)
                if(data == receiverOut):
                    numOfCorrectOutputs += 1
            probabilities.append(1 - (numOfCorrectOutputs/self.numOfInputs))
            input.close()

        u.probVsSNR([i/10.0 for i in range(1, 100, 1)], probabilities)
    
    '''def runWithHammingCode(self):
        u = Utils() 
        self.encodeAllWithHamming()
        allDemodulated = open('demodulated.txt', 'w')
        for i in range(1, 100, 100):
            numOfCorrectOutputs = 0
            AWGNsigma = i / 10.0
            print('for AWGNSgima =', AWGNsigma)
            self.wirelessChannel.setSigma(1/AWGNsigma)
            with open('encoded.txt', 'r') as content_file:
                content = content_file.read()
                for data in [content[i:i+2] for i in range(0, len(content), 2)] :
                    transmitterOut = self.transmitter.modulate(data)
                    afterChannelGainApplied = self.wirelessChannel.applyChannelGain(transmitterOut)
                    wirelessChannelOut = self.wirelessChannel.applyAWGN(afterChannelGainApplied)
                    receiverOut = self.receiver.demodulate2(wirelessChannelOut)
                    allDemodulated.write(receiverOut)

            with open('demodulated.txt', 'r') as content_file :
                content = content_file.read()
                for data in [content[i:i+7] for i in range(0, len(content), 7)] :


            print('pppp', self.probabilites)
            u = Utils()
            u.probVsSNR([i/10.0 for i in range(1, 100, 1)], self.probabilites)'''

    def encodeAllWithHamming(self):
        input = open("input.txt", "r") 
        output = open("encoded.txt", "w")
        while True : 
            line1 = input.readline().rstrip()
            line2 = input.readline().rstrip()
            if not (line2 or line1): break
            encoded = self.transmitter.encodeHamming(map(int, line1 + line2))
            mystring = ""
            for bit in encoded:
                mystring += str(bit)
            output.write(mystring)
        input.close()
        output.close()

def main() :
    w = WirelessSystem(10000)
    #w.encodeAllWithHamming()
    #w.runForLinePlot()
    #w.runForScatterPlot()
    #w.runWithHammingCode()
    #w.runWithHammingCode()
    #w.runForScatterPlot16()
    w.runForLinePlot16()

        

if __name__== "__main__":
      main()
        



        