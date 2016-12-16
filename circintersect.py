from graphics import *
import math
 
def main():
     
        #with 600x300 mapping 25px = 1 Coords
        win = GraphWin('Circle intersection',600,300)
        win.setCoords(0,0,24,12)
        win.setBackground('White')
         
############## Depict Map  ##############
         
        #Chart background with X,Y center line
        chartBG = Rectangle(Point(1,11),Point(11,1))
        chartBG.setFill('grey')
        chartBG.draw(win)
         
        Line(Point(6,1),Point(6,11)).draw(win)
        Line(Point(1,6),Point(11,6)).draw(win)
         
        # indicator bar 12.5px (0.5 Coord each)
        for i in range(2,23):
            i = i/2
            Line(Point(0.75,i),Point(1.25,i)).draw(win)
            Line(Point(i,10.75),Point(i,11.25)).draw(win)
         
         
        # number bar
        z = q = 6
         
        for i in range(0,11):
            num = Text(Point(0.5,z),i)
            num.setSize(6)
            num.draw(win)
             
            num2 = Text(Point(z,11.5),i)
            num2.setSize(6)
            num2.draw(win)
             
            num3 = Text(Point(q,11.5),i*-1)
            num3.setSize(6)
            num3.draw(win)
             
            num3 = Text(Point(0.5,q),i*-1)
            num3.setSize(6)
            num3.draw(win)
             
            z = z+0.5  
            q = q-0.5
             
############## Depict Interface ##############
         
        #introduction
        intro1 = Text(Point(17.40,10.75),'Program to calculate X value where')
        intro1.setStyle('bold')
        intro1.draw(win)
         
        intro2 = Text(Point(15.8,10),'Y intersection with circle.')
        intro2.setStyle('bold')
        intro2.draw(win)
         
        #Radius entry
        Text(Point(15.75,8.5),'Circle radius (value 1-10): ').draw(win)
        inputR = Entry(Point(14,7.5),10)
        inputR.setText('0')
        inputR.draw(win)
         
        #Y Line entry
        Text(Point(18,6),'Horizon line intersection (value 10 to -10): ').draw(win)
        inputY = Entry(Point(14,5),10)
        inputY.setText('0')
        inputY.draw(win)
         
        #X Result entry
        Text(Point(14.5,3.5),'X intersection at: ').draw(win)
        Text(Point(12.2,2.70),'+').draw(win)
        Text(Point(12.2,2.25),'-').draw(win)
         
        answerX = Entry(Point(14.5,2.5),10)
        answerX.setText('?')
        answerX.draw(win)
         
        #Fake button Entry     
        Fbutton = Rectangle(Point(19,2),Point(23.5,0.5))
        Fbutton.setFill('green')
        Fbutton.draw(win)
         
        FbuttonT =  Text(Point(21.25,1.25),'Find Answer!')
        FbuttonT.draw(win)
         
############## Calculation ##############
 
        # pause for input
        win.getMouse()
         
        # get variable
        R = eval(inputR.getText())
        Y = eval(inputY.getText())
         
        # calculate and
        X = math.sqrt(R**2-Y**2)
         
        # force only 2 decimal
        X = round(X,2)
 
############## Output  ##############
         
        # print answer in entry box
          
        answerX.setText(X)
         
        # depict circle
        R = R/2     # because 1Coords = 1/2 unit in map
        resultC = Circle(Point(6,6),R)
        resultC.setFill('yellow')
        resultC.draw(win)
         
        # re-draw the X,Y because circle overlap it
        Line(Point(6,1),Point(6,11)).draw(win)
        Line(Point(1,6),Point(11,6)).draw(win)
         
        # depict Y intersection line
        Y = Y/2+6       # because 1Coords = 1/2 unit in map
        lineY = Line(Point(1,Y),Point(11,Y))
        lineY.setFill('green')
        lineY.draw(win)
         
        # depict both X point in Map
        X = X/2         # because 1Coords = 1/2 unit in map
        Xa = X+6        # make it both start at center of Map (position Coord=6)
        Xb = 6-X
         
        resultPa = Circle(Point(Xa,Y),0.1)
        resultPa.setFill('red')
        resultPa.draw(win)
         
        resultPb = Circle(Point(Xb,Y),0.1)
        resultPb.setFill('red')
        resultPb.draw(win)
 
        FbuttonT.setText('Quit')
                 
        #pause for exit
        win.getMouse()
        win.close()
     
main()
