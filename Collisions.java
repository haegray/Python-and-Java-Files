import javax.swing.*;
import java.awt.*;
import java.util.*;

class Ball {
    // the position, speed and size of the balls
    private double x, y, dx, dy;
    private static final int DIAMETER = 25;
    
    // the color of the ball
    private Color color;

    // sets up a randomly colored, positioned and moving ball
    public Ball( ) {
        Random r = new Random();
        x = r.nextFloat() * 500;
        y = r.nextFloat() * 500;

        dx = r.nextFloat() * 300 - 150;
        dy = r.nextFloat() * 300 - 150;

        color = new Color(r.nextInt(256), r.nextInt(256), r.nextInt(256));
    }

    // draw the ball to the screen
    public void draw(Graphics g) {
        g.setColor(color);
        g.fillOval((int) x, (int) y, DIAMETER, DIAMETER);
    }

    // check if twe balls have collided with each other
    boolean collides(Ball other) {
        // add your code here!
    	double distance = Math.sqrt(
                ((x - other.x) * (x - other.x))
              + ((y - other.y) * (y - other.y))
               );
    if (distance < DIAMETER/2 + other.DIAMETER/2)
    {
        return true;
    }else{
        return false;
    
    }
    }

    // update this balls position - it is given an array of
    // all the other balls as well
    public void update(double dt, Ball balls []) {
        // update the position of the ball
        x += (dx * dt);
        y += (dy * dt);

        // check collisions with the walls
        if (y<0) {
            dy = Math.abs(dy);
        }
        if ((y + DIAMETER) > 500) {
            dy = -Math.abs(dy);
        }
        if (x < 0) {
            dx = Math.abs(dx);
        }
        if ((x + DIAMETER) > 500) {
            dx = -Math.abs(dx);
        }

        // check if we hit another ball
        for (Ball b : balls) {
            // if this is the same ball, don't check for collision with itself!
            if (this == b) {
                continue;
            }
            
            // call the collides function above to check for collision
            if (collides(b)) {
                // swap the speeds in response to the collision
                double new_dx1 = b.dx;
                double new_dy1 = b.dy;
                double new_dx2 = dx;
                double new_dy2 = dy;
                
                // update them
                dx = new_dx1;
                dy = new_dy1;
                b.dx = new_dx2;
                b.dy = new_dy2;
                
                // move them a little - this avoids overlapping circles
                x += dx * .01;
                y += dy * .01;
                b.x += b.dx * .01;
                b.y += b.dy * .01;
                
                // change color randomly
                Random r = new Random( );
                color = new Color(r.nextInt(256), r.nextInt(256), r.nextInt(256));
            }
        }
    }
}

class GameWorld extends JComponent {
    // keep an array of balls and the amount of elapsed time
    private Ball balls[];
    private long elapsed;

    // set up some number of balls
    public GameWorld(int count) {
        elapsed = new Date().getTime();
        balls = new Ball [count];
        for (int i = 0; i < count; i++) {
            balls[i] = new Ball();
        }
    }

    @Override
    public void paintComponent(Graphics g) {
        // draw a black background
        g.setColor(Color.black);
        g.fillRect(0, 0, 500, 500);

        // draw all of the balls
        for (Ball f : balls) {
            f.draw(g);
        }

        // update everything
        long time_now = new Date().getTime();
        double seconds = (time_now - elapsed) / 1000.0;
        elapsed = time_now;
        for (Ball f : balls) {
            f.update(seconds, balls);
        }

        // force an update
        revalidate();
        repaint();
    }
}

public class Collisions {

    public static void main(String args[]) {
        // create and set up the window.
        JFrame frame = new JFrame("Collisions!");

        // make the program close when the window closes
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // add the GameWorld component
        frame.add(new GameWorld(20));

        // display the window.
        frame.setSize(510, 530);
        frame.setVisible(true);
    }
}
