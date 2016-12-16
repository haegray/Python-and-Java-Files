// Helena Gray

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JToolBar;

// game window
public class GameWindow extends JFrame implements ActionListener, Runnable {

    private JLabel scoreLabel = new JLabel("Score: 0");
    private JLabel highScoreLabel = new JLabel("High Score: 0");
    private JLabel timerLabel = new JLabel("Time Left: 0");

    private JPanel gamePanel = new JPanel(new GridLayout(4, 4));
    private JButton newGameButton = new JButton("New Game");
    private HoleButton[] buttons = new HoleButton[4 * 4];

    // Initialize our game window
    public GameWindow() {

        // Initialize window properties
        setTitle("Whack a Mole!");
        setSize(700, 700);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Initialize menus
        JToolBar toolBar = new JToolBar();
        add(BorderLayout.PAGE_START, toolBar);

        newGameButton.addActionListener(this);
        toolBar.add(newGameButton);
        toolBar.addSeparator();
        toolBar.add(scoreLabel);
        toolBar.addSeparator();
        toolBar.add(highScoreLabel);
        toolBar.addSeparator();
        toolBar.add(timerLabel);

        // Initialize the game buttons
        for (int i = 0; i < buttons.length; i++) {
            buttons[i] = new HoleButton(this);
            gamePanel.add(buttons[i]);
        }

        add(BorderLayout.CENTER, gamePanel);
    }

    // Initialize a new game
    private void doNewGame() {
        // Choose a difficulty
        String[] difficulties = {"Easy", "Medium", "Hard"};

        GameGlobals.difficultyLevel = JOptionPane.showOptionDialog(this, "Select Difficulty", "Select Difficulty", 0, JOptionPane.WARNING_MESSAGE, null, difficulties, difficulties[0]);
        GameGlobals.isGameOver = false;
        GameGlobals.currentScore = 0;

        // Activate the buttons and start a new game
        for (HoleButton button : buttons) {
            button.activate();
        }

        // Start the timer
        GameGlobals.currentTime = 20;
        newGameButton.setEnabled(false);
        scoreLabel.setText("Score: " + GameGlobals.currentScore);

        new Thread(this).start();
    }

    // Handle button clicks (not the HOLE, but the menus)
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand().equalsIgnoreCase("New Game")) {
            doNewGame();
        }
    }

    // This will be our timer
    @Override
    public void run() {
        timerLabel.setText("Time Left: " + GameGlobals.currentTime);

        while (GameGlobals.currentTime > 0) {
            try {
                Thread.sleep(1000);
            } catch (Exception e) {
                e.printStackTrace(System.out);
            }

            GameGlobals.currentTime--;
            timerLabel.setText("Time Left: " + GameGlobals.currentTime);
        }

        GameGlobals.isGameOver = true;
        newGameButton.setEnabled(true);

        JOptionPane.showMessageDialog(this, "Game Over! Thanks for Playing!");
    }

    // This will redisplay the scores, called upon the hole button when clicked
    public void updateScores() {
        scoreLabel.setText("Score: " + GameGlobals.currentScore);

        if (GameGlobals.currentScore > GameGlobals.highScore) {
            GameGlobals.highScore = GameGlobals.currentScore;
            highScoreLabel.setText("High Score: " + GameGlobals.highScore);
        }
    }

    // Entry point of the program, show the game window
    public static void main(String[] args) {
        new GameWindow().setVisible(true);
    }
}
