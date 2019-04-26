from __future__ import division
from Transmitter import Transmitter
from  Receiver import Receiver
from WirelessChannel import WirelessChannel
from Utils import Utils
#import matplotlib.pyplot as plt

class WirelessSystem:
    def __init__(self, numOfInputs):
        self.transmitter = Transmitter()
        self.receiver = Receiver()
        self.wirelessChannel = WirelessChannel(0.1)
        self.numOfInputs = numOfInputs
        self.sigmaValues = [10, 1, 0.1]
        self.reveivedPoints = []
        self.colors = ['purple', 'yellow', 'orange']
        self.hammingProbs = []
        self.qpskProbs = []
    
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
                point = self.transmitter.modulate(data)
                (hI, hQ) = self.wirelessChannel.applyChannelGain(point)
                self.wirelessChannel.applyAWGN(point)
                self.reveivedPoints.append(point)

            u.showScatterPlot(self.reveivedPoints ,AWGNsigma, self.colors[i])
            input.close()


    def runForScatterPlot16(self):
        u = Utils() 
        probabilities = []
        for i in range(len(self.sigmaValues)):
            self.reveivedPoints = []
            input = open("input.txt", "r")
            numOfCorrectOutputs = 0
            AWGNsigma = self.sigmaValues[i]
            self.wirelessChannel.setSigma(1/AWGNsigma)
            cntr = 0
            for line in input:
                if(cntr == 0):
                    data = line.rstrip()
                    cntr += 1
                    continue
                else:
                    data += line.rstrip()
                    cntr = 0
                    point = self.transmitter.modulate16QAM(data)
                    (hI, hQ) = self.wirelessChannel.applyChannelGain(point)
                    self.wirelessChannel.applyAWGN(point)
                    self.reveivedPoints.append(point)

            u.showScatterPlotQAM(self.reveivedPoints ,AWGNsigma, self.colors[i])
            input.close()
               
    def runForLinePlot(self):
        u = Utils() 
        probabilities = []
        for i in range(1, 100, 1):
            input = open("input.txt", "r")
            numOfCorrectOutputs = 0
            SNR = i / 10
            print('i=', i, 'for AWGNSgima =', 1/SNR)
            self.wirelessChannel.setSigma(1/SNR)
            for line in input:
                data = line.rstrip()
                point = self.transmitter.modulate(data)
                (hI, hQ) = self.wirelessChannel.applyChannelGain(point)
                self.wirelessChannel.applyAWGN(point)
                self.receiver.removeChannelImpact(point, hI, hQ)
                receiverOut = self.receiver.demodulate2(point)
                if(data == receiverOut):
                    numOfCorrectOutputs += 1
            probabilities.append(1 - (numOfCorrectOutputs/self.numOfInputs))
            input.close()

        print(probabilities)
        self.qpskProbs = probabilities
        u.probVsSNR([(i/10.0) for i in range(1, 100, 1)], probabilities)


    def runForLinePlot16(self):
        u = Utils() 
        probabilities = []
        for i in range(1, 100, 1):
            input = open("input.txt", "r")
            numOfCorrectOutputs = 0
            SNR = i / 10
            print('i=', i, 'for AWGNSgima =', 1/SNR)
            self.wirelessChannel.setSigma(1/SNR)
            cntr = 0
            for line in input:
                if(cntr == 0):
                    data = line.rstrip()
                    cntr += 1
                    continue
                else :
                    cntr = 0
                    data += line.rstrip()
                    point = self.transmitter.modulate16QAM(data)
                    (hI, hQ) = self.wirelessChannel.applyChannelGain(point)
                    self.wirelessChannel.applyAWGN(point)
                    self.receiver.removeChannelImpact(point, hI, hQ)
                    receiverOut = self.receiver.demodulate16(point)
                    if(data == receiverOut):
                        numOfCorrectOutputs += 1
            probabilities.append(1 - (numOfCorrectOutputs/(self.numOfInputs/2)))
            input.close()

        u.probVsSNR([i/10.0 for i in range(1, 100, 1)], probabilities)
    
    def runWithHammingCode(self):
        u = Utils() 
        probabilities = []
        self.encodeAllWithHamming()
        for i in range(1, 100, 1):
            allDemodulated = open('demodulated.txt', 'w')
            SNR = i / 10.0
            print('for AWGNSgima =', 1/SNR)
            self.wirelessChannel.setSigma(1/SNR)
            content_file = open('encoded.txt', 'r')
            content = content_file.read()
            for data in [content[i:i+2] for i in range(0, len(content), 2)] :
                point = self.transmitter.modulate(data)
                (hI, hQ) = self.wirelessChannel.applyChannelGain(point)
                self.wirelessChannel.applyAWGN(point)
                self.receiver.removeChannelImpact(point, hI, hQ)
                receiverOut = self.receiver.demodulate2(point)
                allDemodulated.write(receiverOut)
            allDemodulated.close()

            self.decodeAll()
            numOfCorrectOutputs = self.reconstructAndCalcCorrectOutputs()
            probabilities.append(1 - (numOfCorrectOutputs/(self.numOfInputs)))

        self.hammingProbs = probabilities
        u.probVsSNR([i/10.0 for i in range(1, 100, 1)], probabilities)
        #plt.plot([i/10.0 for i in range(1, 100, 1)], probabilities,  color='green')
        #plt.plot([i/10.0 for i in range(1, 100, 1)], self.qpskProbs)
        #plt.show()

    def runForScatterPlotHamming(self):
        u = Utils() 
        probabilities = []
        self.receivedPoints = []
        for i in range(len(self.sigmaValues)):
            AWGNsigma = self.sigmaValues[i]
            self.wirelessChannel.setSigma(1/AWGNsigma)
            content_file = open('encoded.txt', 'r')
            content = content_file.read()
            for data in [content[x:x+2] for x in range(0, len(content), 2)] :
                point = self.transmitter.modulate(data)
                (hI, hQ) = self.wirelessChannel.applyChannelGain(point)
                self.wirelessChannel.applyAWGN(point)
                self.reveivedPoints.append(point)

            u.showScatterPlot(self.reveivedPoints , AWGNsigma, self.colors[i])
        content_file.close()


    def encodeAllWithHamming(self):
        input = open("input.txt", "r") 
        output = open("encoded.txt", "w")
        cntr = 0
        for line in input: 
            if(cntr == 0):
                data = line.rstrip()
                cntr +=1
                continue
            else:
                data += line.rstrip()
                cntr = 0
                encoded = self.transmitter.encodeHamming(map(int, data))
                mystring = ""
                for bit in encoded:
                    mystring += str(bit)
                output.write(mystring)
        input.close()
        output.close()
    
    def decodeAll(self):
        demod = open('demodulated.txt', 'r')
        decodedFile = open("decoded.txt", "w")
        lines = demod.read()
        for data in [lines[i:i+7] for i in range(0, len(lines), 7)] :
            decoded = self.receiver.decodeHamming(map(int, data))
            actualData = data[0:4]
            mystring = ""
            for bit in decoded:
                mystring += str(bit)
            decodedFile.write(actualData + mystring)
                    
        decodedFile.close()
        demod.close()
    
    def reconstructAndCalcCorrectOutputs(self):
        numOfCorrects = 0
        counter = 0
        decodedFile = open('decoded.txt', 'r')
        lines = tuple(open('input.txt', 'r'))
        content = decodedFile.read()
        for line in [content[i:i+7] for i in range(0, len(content), 7)] :
            actualData = line[0 : 4]
            syndromes = line[4:7]
            inputLine1 = lines[counter].rstrip() 
            inputLine2 = lines[counter + 1].rstrip()
            correctedOutput = self.receiver.findAndCorrectError(syndromes, actualData)
            if(correctedOutput[0 : 2] == inputLine1):
                numOfCorrects += 1
            if(correctedOutput[2 : 4] == inputLine2):
                numOfCorrects += 1
            counter += 2

        return numOfCorrects
    

def main() :
    w = WirelessSystem(10000)

    w.runForLinePlot()
    w.runForScatterPlot()

    #w.runWithHammingCode()
    #w.runForScatterPlotHamming()


    #w.runForScatterPlot16()
    #w.runForLinePlot16()

        

if __name__== "__main__":
      main()
        



        