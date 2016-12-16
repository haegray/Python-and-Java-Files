import javax.swing.*;
import java.io.*;
import java.awt.event.*;
import java.util.Scanner;
import javax.swing.filechooser.*;

public class FileOpener extends JPanel implements ActionListener {
	
	private Password1 p1;
	JButton decodeButton, encodeButton;
	JFileChooser fc;
	JTextArea log;
	Scanner in = new Scanner(System.in);
	JFrame frame;
	File file;
	int count;
	String key;

	public FileOpener(){
		// create and set up the window.
		frame = new JFrame("Open Your File");
		

		// make the program close when the window closes
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		// create the box layout
		frame.getContentPane( ).setLayout(new BoxLayout(frame.getContentPane( ), BoxLayout.Y_AXIS));

        //label prompting user for input
        JLabel label1 = new JLabel ("Would you like to encode or decode your file?", JLabel.CENTER);
        frame.getContentPane().add(label1);
		
		//create a filer chooser
		fc = new JFileChooser();
		
		// add a button object
		decodeButton = new JButton("Decode");
		decodeButton.addActionListener(this);
		frame.getContentPane( ).add(decodeButton);

		encodeButton = new JButton("Encode");
		encodeButton.addActionListener(this);
		frame.getContentPane( ).add(encodeButton);
		

		// display the window.
		frame.pack( );
		frame.setVisible(true);
	}
	public void actionPerformed(ActionEvent e) {
		p1 = Password1.createAndShowGUI();
		
		//Handle open button action.
		if (e.getSource() == encodeButton) {
			p1.setOperation("encode");
			 frame.dispose();
			int returnVal = fc.showOpenDialog(FileOpener.this);
			if (returnVal == JFileChooser.APPROVE_OPTION ) {
					file = fc.getSelectedFile();
					p1.setFile(file);	
			}
			
			//Handle save button action.
		} else if (e.getSource() == decodeButton) {
			p1.setOperation("decode");
			 frame.dispose();
			int returnVal = fc.showOpenDialog(FileOpener.this);
			if (returnVal == JFileChooser.APPROVE_OPTION) {
					file = fc.getSelectedFile();
					p1.setFile(file);	
			}

			}
	}


public static void main(String args[]) {
	//Schedule a job for the event dispatch thread:
    //creating and showing this application's GUI.
  FileOpener f = new FileOpener();
  
}    
}