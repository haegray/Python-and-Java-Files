//Helena Gray
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
import javax.swing.ImageIcon;
import javax.swing.JButton;

// A hole is where the mole comes out
public class HoleButton extends JButton implements ActionListener, Runnable {

    private GameWindow gameWindow;
    private Random random = new Random();

    // Initialize  button
    public HoleButton(GameWindow gameWindow) {
        setEnabled(false);
        setIcon(new ImageIcon("mole.png"));
        this.gameWindow = gameWindow;
        addActionListener(this);
    }

    // When clicked, add score to the player, but this is only clickable when it is enabled
    @Override
    public void actionPerformed(ActionEvent e) {
        if (GameGlobals.isGameOver) {
            return;
        }

        // Mole got hit.. add a score, hide the mole
        hideMole();

        GameGlobals.currentScore++;
        gameWindow.updateScores();
    }

    // When new game starts, the button gets activated and starts running
    // until the game is over
    public void activate() {
        hideMole();
        setEnabled(false);

        new Thread(this).start();
    }

    // Hide the mole
    private void hideMole() {
        setIcon(null);
        setEnabled(false);
    }

    // Show the mole
    private void showMole() {
        setIcon(new ImageIcon("mole.png"));
        setEnabled(true);
    }

    // generate a random number
    private int getRandomBetween(int min, int max) {
        return random.nextInt((max - min) + 1) + min;
    }

    // runs until game is over, what this does is it randomly
    // shows a mole on this hole and the mole stays out for a random time
    @Override
    public void run() {

        while (!GameGlobals.isGameOver) {
            try {
                // Hide for a random time
                Thread.sleep(getRandomBetween(5, 10) * 1000);

                // Show self for a random time depending on difficulty
                if (!GameGlobals.isGameOver) {
                    showMole();

                    switch (GameGlobals.difficultyLevel) {
                        case 0:
                            Thread.sleep(getRandomBetween(5, 10) * 1000);
                            break;
                        case 1:
                            Thread.sleep(getRandomBetween(1, 5) * 1000);
                            break;
                        case 2:
                            Thread.sleep(1000);
                            break;
                    }
                }

                // Hide again
                hideMole();
                
                // Hide for a random time
                Thread.sleep(getRandomBetween(5, 10) * 1000);
            } catch (Exception e) {
                e.printStackTrace(System.out);
            }
        }

        hideMole();
    }
}
