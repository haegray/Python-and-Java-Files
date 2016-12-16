#sphereRadiusandVolume.py

from math import *
 
def main():
    print("To find the volume and surface area of a sphere I need to know the radius.")
 
    r = eval(input("Please enter the radius of the sphere in cm: "))
 
    area = (4 * pi * r**2)
    volume = ((4 * pi * r**3) / 3)
    print()
    print("The volume of the sphere is", volume, "cubic cm",)
    print("The area of the sphere is", area, "square cm")
main()

#IOP:
#>>> ================================ RESTART ================================
#>>> 
#To find the volume and surface area of a sphere I need to know the radius.
#Please enter the radius of the sphere in cm: 3
#The volume of the sphere is 113.09733552923255 cubic cm
#The area of the sphere is 113.09733552923255 square cm
