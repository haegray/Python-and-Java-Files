####futval
from graphics import *

def futbal(amount,rate):
    for year in range(1,11):
        amount = amount * (1 + rate/100.0)
        r=Rectangle(Point((year-1)*40,399),
                    Point(40 + (year -1) * 40, -99+ 400 - 400*(amount/10000)))
        r.draw(win)
        yearLabel=Text(Point((2*year-1))/20.0,350),str(year))
        print('In year {0:2} amount is ${1:0.2f}'.format(year,amount))


def futvalGraph(amount,rate):
    win-GraphWin("Future Value", height=400, width=400)
    bar1=Rectangle(Point(2,399), Point(40,400-400*(amount/10000)))
    bar1.draw(win)
