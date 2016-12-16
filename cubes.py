from math import *

class Cube:

    def __init__(self,r):
        self.radius = r
        self.area= 0
        self.volume= 0


    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        r=self.radius
        self.area= (r*r)*6
        return (self.area)

    def getVolume(self):
        r = self.radius
        self.volume = (r**3)
        return (self.volume)

def main():
    r= float(input("Enter radius:"))
    s = Cube(r)

    print("The surface area of the cube is:", s.surfaceArea())
    print("The volume of the cube is: ", s.getVolume())

    if __name__ == '__main__':
        main()
