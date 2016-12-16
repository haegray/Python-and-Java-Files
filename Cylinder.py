import math

class Cylinder:
    def __init__(self, radius, height):
      self.radius = radius
      self.height = height
    def getRadius(self):
        return self.radius
    def getHeight(self):
        return self.height

    def Volume(self):
        r = self.radius
        h = self.height
        self.volume = ((h) * 3.14 * (r*r))
        return (self.volume)
    
    def surfaceArea(self):
        r=self.radius
        h=self.height
        self.area= (2*3.14*r*h) * (2* 3.14 * (r*r))
        return (self.area)

def main():
    radius, height = float(input("Enter radius and height."))
    s = Cylinder(radius, height)
    
    print("The radius of the sphere is:", s.getRadius())
    print("The height of the sphere is:", s,getHeight())
    print("The surface area of the sphere is:", s.surfaceArea())
    print("The volume of the sphere is: ", s.getVolume())

    if __name__ == '__main__':
        main()
