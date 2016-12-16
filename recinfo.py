import math
from graphics import *
 
def main():
     
##### SETUP GraphWin   
 
    win = GraphWin('Rectangle Information',500,300)
    win.setCoords(0, 0, 40, 24)     #1 coords = 12.5 px
     
##### RENDER GUI
     
    # field = 22x22 coords
    field = Rectangle(Point(1,23),Point(23,1))
    field.setFill('white')
    field.setWidth(0)
    field.draw(win)
     
    invite = Text(Point(12,12),'Draw Here')
    invite.setSize(32)
    invite.setFill('grey')
    invite.setFace('courier')
    invite.setStyle('italic')
    invite.draw(win)
     
    # draw indicator grey table
    for i in range(2,23):
        guide = Line(Point(i,23),Point(i,1))
        guide.setFill('grey')
        guide.draw(win)
         
        guide = Line(Point(23,i),Point(1,i))
        guide.setFill('grey')
        guide.draw(win)
         
    # print panel introduction & result box
    intro1 = Text(Point(31,22),'Click inside left field to')
    intro1.setStyle('bold')
    intro1.draw(win)
     
    intro2 = intro1.clone()
    intro2.setText('draw rectangle and')
    intro2.move(-1,-1.5)
    intro2.draw(win)
     
    intro3 = intro2.clone()
    intro3.setText('receive perimeter and')
    intro3.move(0.8,-1.5)
    intro3.draw(win)
     
    intro4 = intro3.clone()
    intro4.setText('area infomation below.')
    intro4.move(0.2,-1.5)
    intro4.draw(win)
        
    # draw entry box and text
    Text(Point(30,14),'Area :').draw(win)
    areaBox = Entry(Point(35,14),7)
    areaBox.setText('???')
    areaBox.draw(win)
     
    Text(Point(28.5,11),'Perimeter :').draw(win)
    perimeterBox = Entry(Point(35,11),7)
    perimeterBox.setText('???')
    perimeterBox.draw(win)
     
     
##### INPUT 
 
    #wait for two mouse click and create point
    p1 = win.getMouse()
    p1.draw(win)
     
    p2 = win.getMouse()
    p2.draw(win)
     
     
##### PROCESS & OUTPUT   
     
    # undraw invite text
    invite.undraw()
     
    #draw rectangle accord to user click
    rec = Rectangle(p1,p2)
    rec.setFill('white')
    rec.draw(win)
     
    # get x,y from both points
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
     
    # find width & length of rectangle
    dx = x1-x2
    dy = y1-y2
     
    # make sure only positive value before calculation
    dx = abs(dx)
    dy = abs(dy)
     
    # use given formula
    area = dx*dy
    perimeter = 2*(dx+dy)
     
    # print result into entry box with 3 decimals
    areaBox.setText(round(area,3))
    perimeterBox.setText(round(perimeter,3))
      
     
##### QUIT
 
    #print quit button
    button = Rectangle(Point(32,1),Point(39,3.5))
    button.setFill('green')
    button.draw(win)
    Text(Point(35.5,2.25),'Quit!').draw(win)
     
    #wait for final click to quit
    win.getMouse()
    win.close()
 
main()
