from graphics import *
 
def main():
    win = GraphWin()
    
    for i in range(5):


        p = win.getMouse()

        tx = p.getX()-10
        ty = p.getY()-10
        bx = p.getX()+10
        by = p.getY()+10

        if tx <= 100:
 
            Rectangle(Point(tx,ty),Point(bx,by)).draw(win)

        elif tx >= 100:
            r = bx - tx
            Circle(Point(tx,ty), 15).draw(win)
 
    Text(Point(100,180),'Click again to quit!').draw(win)
    win.getMouse()
    win.close()
main()
