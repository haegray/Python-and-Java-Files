from graphics import *
 
def main():
    win = GraphWin('Archery Target',300,300)
    center = Point(150,150)
 
    w = Circle(center,100)
    w.setFill('White')
    w.draw(win)
 
    b = Circle(center,80)
    b.setFill('Black')
    b.draw(win)
 
    bl = Circle(center,60)
    bl.setFill('Blue')
    bl.draw(win)
 
    r = Circle(center,40)
    r.setFill('Red')
    r.draw(win)
 
    y = Circle(center,20)
    y.setFill('Yellow')
    y.draw(win)
 
    win.getMouse()
    win.close()
main()
