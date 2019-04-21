from Point import Point

class Receiver:
    def __init__(self):
        self.point00 = Point(-0.707, -0.707)
        self.point01 = Point(-0.707, 0.707)
        self.point10 = Point(0.707, -0.707)
        self.point11 = Point(0.707, 0.707)

    def demodulate(self, point):
        distances = []
        distances.append(point.distance(self.point00))
        distances.append(point.distance(self.point01))
        distances.append(point.distance(self.point10))
        distances.append(point.distance(self.point11))
        index = (distances.index(min(distances)))
        if(index == 0):
            return "00"
        elif(index == 1):
            return "01"
        elif(index ==2):
            return "10"
        else:
            return "11"
        
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

        

       
