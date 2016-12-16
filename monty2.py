from random import randrange
from graphics import *
 
 
class Door:
    '''create a class for door object.'''
     
    def __init__(self,win,center,width,height,label):
        '''provide attribute of every door object'''
         
        #self.secret use for remember this is a serect door or not
        #for initial value start with 0
        # 0 = not this door
        # 1 = this is scret door
        self.secret = 0
         
        #self.hasClick turn to 1 if user click this door by self.clicked()
        self.hasClick = 0
         
        #get X,Y from center and find border of the door
        x,y = center.getX(),center.getY()
        self.xmin, self.xmax = x-width/2,x+width/2
        self.ymin, self.ymax = y-height/2,y+height/2
         
        #draw a door border
        self.rec = Rectangle(Point(self.xmin,self.ymax),Point(self.xmax,self.ymin))
        self.rec.setFill("yellow")
        self.rec.setWidth(0)
        self.rec.draw(win)
         
        #draw label
        self.label1= Rectangle(Point(x-(width/2.8),y+(height/2.35)),Point(x+(width/3.2),y++(height/3.6)))
        self.label1.setFill("red")
        self.label1.setWidth(0)
        self.label1.draw(win)
         
        #draw text on label
        self.text = Text(Point(x,y+(height/2.8)),label)
        self.text.setSize(10)
        self.text.draw(win)
         
     
    def setSecret(self):
        '''Set this door to a secret door.'''
        self.secret = 1
        print()
         
     
    def turnGreen(self):
        '''Turn door color to green to present this is a correct door.'''
        self.rec.setFill(color_rgb(51,229,70))
        self.label1.setFill(color_rgb(62,200,0))
         
         
    def turnRed(self):
        '''Turn door to red if user click on wrong door.'''
        self.rec.setFill(color_rgb(234,53,65))
        self.label1.setFill(color_rgb(240,49,61))
         
         
    def clicked(self,p):
        '''Remember if door has click by user
        and also return Bool data'''
        if self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax:
            self.hasClick = 1
         
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
     
     
    def reveal(self):
        '''Key door feature. It will check self.secret and self.hasClcik
        and respond accordingly to both action.'''
         
        #if user click on a correct door
        if self.secret == 1 and self.hasClick == 1:
            #turn door to green and return a win message
            self.turnGreen()
            return 'win'
         
        #if user click on wrong door turn it to red no need to respond
        elif self.secret == 0 and self.hasClick == 1:
            self.turnRed()
         
        #reveal itself as secret door if user didnt pick it up   
        elif self.secret ==1 and self.hasClick ==0:
            self.turnGreen()
            return 'secret'
             
             
             
def main():
    '''Main program start here.'''
     
    win,msg,d1,d2,d3 = drawGUI()
    secretDoor(d1,d2,d3)
    getInput(win,d1,d2,d3)
    result(msg,d1,d2,d3)
    exit(win)
     
     
     
def drawGUI():
    '''Set up all GUI on the screen.'''
     
    #setup windows
    win = GraphWin('Three Button Monte',390,300)
    win.setCoords(0,0,130,100)
    win.setBackground('white')
     
    #draw 3 door
    d1 = Door(win,Point(25,60),30,53,'Door 1')
    d2 = Door(win,Point(65,60),30,53,'Door 2')
    d3 = Door(win,Point(105,60),30,53,'Door 3')
     
    #draw title of program
    title = Text(Point(65,95),'Three Button Monte')
    title.setSize(17)
    title.draw(win)
     
    #draw message box
    msgBox = Rectangle(Point(10,25),Point(120,9))
    msgBox.setFill('yellow3')
    msgBox.setWidth(0)
    msgBox.draw(win)
     
    #draw message to invite user
    msg = Text(Point(65,17),'Guess which one is a correct exit door?')
    msg.setSize(13)
    msg.draw(win)
 
    return win,msg,d1,d2,d3
     
 
 
def secretDoor(d1,d2,d3):
    '''Random number from 1-3 and mark a secret door.'''
     
    i = randrange(1,4)
     
    if i == 1: d1.setSecret()
    elif i == 2 : d2.setSecret()
    else: d3.setSecret()
 
 
 
def getInput(win,d1,d2,d3):
    '''Wait for mouse click and continue to loop until user click on
    any door.'''
     
    p = win.getMouse()
      
    while not d1.clicked(p) and not d2.clicked(p) and not d3.clicked(p):
        p = win.getMouse()       
     
     
 
def result(msg,d1,d2,d3):
    '''This is Conclusion, Door will change its color (red,green)
    and display message result on screen either win or lose.'''
     
    #door reveal its color accord to user click and secret door
    x = d1.reveal()
    y = d2.reveal()
    z = d3.reveal()
     
    #if any door object return a win msg display it
    if x == 'win' or y == 'win' or z == 'win':
        msg.setText('You win!\n')
     
    #if user pick up wrong door, check which door is secret door and tell him
    else:
        if x == 'secret': wayout = '1'
        elif y == 'secret': wayout = '2'
        else: wayout = '3'
              
        msg.setText('You lose! the correct door is door {}!\
        \n'.format(wayout))
 
 
#### QUIT
 
    #print quit button
    button = Rectangle(Point(32,1),Point(39,3.5))
    button.setFill('green')
    button.draw(win)
    Text(Point(35.5,2.25),'Quit!').draw(win)
     
    #wait for final click to quit
    win.getMouse()
    win.close()
 
 
if __name__ == '__main__': main()
