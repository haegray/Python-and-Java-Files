import javax.swing.*;
import java.awt.*;

// the gameworld is a component, so it can be added to a GUI program
class GameWorld extends JComponent {
    @Override
    // overriding this method changes how it is shown
    public void paintComponent(Graphics g) {
        // just draw a black line on the window
        g.setColor(Color.black);
        //H
        g.drawLine(100, 100, 100, 300);
        g.drawLine(100, 100, 125, 100);
        g.drawLine(125, 100, 125, 175);
        g.drawLine(125, 175, 175, 175);
        g.drawLine(125, 200, 175, 200);
        g.drawLine(125, 200, 125, 300);
        g.drawLine(100, 300, 125, 300);
        g.drawLine(175,200, 175, 300);
        g.drawLine(175, 300, 200, 300);
        g.drawLine(200, 100, 200, 300);
        g.drawLine(175, 100, 175, 175);
        g.drawLine(175, 100, 200, 100);
        
        
        //G
        
        g.drawLine(275, 300, 225, 200);
        g.drawLine(225, 200, 275, 100);
        g.drawLine(275, 300, 325, 200);
        g.drawLine(325, 200, 275, 200);
        g.drawLine(275, 200, 275, 215);
        g.drawLine(275, 215, 295, 215);
        g.drawLine(295, 215, 275, 260);
        g.drawLine(275, 260, 250, 200);
        g.drawLine(250, 200, 275, 150);
        g.drawLine(275, 100, 325, 185);
        g.drawLine(325, 185, 300, 185);
        g.drawLine(300, 185, 275, 150);
        
    }
}

public class graphicsExercise {
    public static void main(String args[]) {
        // create and set up the window.
        JFrame frame = new JFrame("Graphics Example!");

        // make the program close when the window closes
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // add the GameWorld component
        frame.add(new GameWorld( ));

        // display the window.
        frame.setSize(500, 500);
        frame.setVisible(true);
    }
}