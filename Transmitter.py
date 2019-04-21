from Point import Point

class Transmitter:
    def modulate(self, input):
        if(input == "00"):
            return Point(-0.707, -0.707)
        elif(input == "01"):
            return Point(-0.707, 0.707)
        elif(input == "10"):
            return Point(0.707, -0.707)
        else :
            return Point(0.707, 0.707)

