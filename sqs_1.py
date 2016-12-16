def sqs():
    from graphics import *
    win = GraphWin()
    shape = Rectangle(Point(50-10,50-10),Point(50 + 10, 50+10))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()
sqs()
