from graphics import *
    

def sqs():
    win = GraphWin()
    shape = Rectangle(Point(50-10,50-10),Point(50 + 10, 50+10))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        p1 = shape.getP1()
        p2 = shape.getP2()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        p1.move(dx,dy)
        p2.move(dx,dy)
        sn=Rectangle(p1,p2)
        sn.draw(win)

        
    win.close()
sqs()
