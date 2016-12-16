from math import sin, cos, radians

def main():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input(
        "Enter the time interval between position calculations: "))
    xpos = 0.0
    ypos = h0
    zenith =0.0

    theta=radians(angle)
    xvel=vel * cos(theta)
    yvel=vel * sin(theta)

    while ypos>= 0.0:
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time *(yvel + yvel1)/2.0
        yvel = yvel1

        if ypos>= zenith:
            zenith = ypos
        
    print("\Distance traveled: {0:0.1f} meters.".format(xpos))
    print("The height the cannon ball reached was %.01f meters." % (zenith))

    main()
