
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;
import java.io.*;
 
/* PasswordDemo.java requires no other files. */
 
public class Password1 extends JPanel
                          implements ActionListener {
	 public String getKey(){
	    	return key;
	    }
	    
	    public void setFile(File file){
	    	this.file = file;
	    }
	    public File getFile(){
	    	return file;
	    }
	    
	    public void setOperation(String operation){
	    	this.operation = operation;
	    }
	    
	    public String getOperation(){
	    	return operation;
	    }
	    
	    public void setName(String name1){
	    	this.name1 = name1;
	    }
	    public String getName(){
	    	return name1;
	    }
	    
	    
	private String key;
    private static String OK = "ok";
 
    private JFrame controllingFrame; //needed for dialogs
    private JPasswordField passwordField;
    private File file;
    private String operation;
    private String name1;
 
    public Password1(JFrame f) {
        //Use the default FlowLayout.
        controllingFrame = f;
 
        //Create everything.
        passwordField = new JPasswordField(10);
        passwordField.setActionCommand(OK);
        passwordField.addActionListener(this);
 
        JLabel label = new JLabel("Enter the key: ");
        label.setLabelFor(passwordField);
 
        JComponent buttonPane = createButtonPanel();
 
        //Lay out everything.
        JPanel textPane = new JPanel(new FlowLayout(FlowLayout.TRAILING));
        textPane.add(label);
        textPane.add(passwordField);
 
        add(textPane);
        add(buttonPane);
    }
 
    protected JComponent createButtonPanel() {
        JPanel p = new JPanel(new GridLayout(0,1));
        JButton okButton = new JButton("OK");
        okButton.setActionCommand(OK); 
        okButton.addActionListener(this);
        p.add(okButton);
        return p;
    }
 
    public void actionPerformed(ActionEvent e) {
    	
    	Scanner in = new Scanner(System.in);
    	int count;
    	
        String cmd = e.getActionCommand();
        controllingFrame.dispose();
 
        if (OK.equals(cmd)) { //Process the password.
            char[] input = passwordField.getPassword();
            
            key = new String(input);
            //Zero out the possible password, for security.
            Arrays.fill(input,'0');
            passwordField.selectAll();
            resetFocus();
        } else {
        	System.out.println("Please enter a key.");
        }
        
        
        if(getOperation().equals("encode")){
        	//get length of key
			String key = getKey();
			int length3 = key.length();
			count = 0;
			int keyAsciiValues[] = new int[length3];
			String name1 ="";
			//get ascii value of each letter in key
			for (int k=0; k<length3; k++){
				char a = key.charAt(k);
				int ascii1 = (int)a;
				//put ascii value of letter in key to array
				keyAsciiValues[k]= ascii1;

			}

			File file2= getFile();
			
			//create a scanner for it
			try{
			in = new Scanner(file2);
			}	
			catch (FileNotFoundException k){
				//the file was not found!
				System.out.println("File could not be opened!");
			}
			//read in message
			String name;
			name = in.nextLine();
			for (int k=0; k<length3; k++){
				char a = key.charAt(k);
				int ascii1 = (int)a;
				//put ascii value of letter in key to array
				keyAsciiValues[k]= ascii1;
			}
			//measure length of code message array
			int length1 = name.length();
			//measures length of strings in code message array
			for(int j=0;j<length1;j++){
				char c = name.charAt(j);
				int ascii = (int)c;
				ascii += keyAsciiValues[count];
				if(c != ' '){
					count++;
				}
				if(count>length3-1){
					count = 0;
				}
				while(ascii>126){
					ascii-= 93;
				}
				char b=(char)ascii;
				if(c == ' '){
					b = ' ';
				}
				name1 += b;
			}
			System.out.println(name1);	
        }
        
        if (getOperation().equals("decode")){

			//get length of key 
			String key = getKey();
			int length3 = key.length();
			count = 0;
			int keyAsciiValues[] = new int[length3];
			String name1 ="";
			//get ascii value of each letter in key
			for (int k=0; k<length3; k++){
				char a = key.charAt(k);
				int ascii1 = (int)a;
				//put ascii value of letter in key to array
				keyAsciiValues[k]= ascii1;
			}

			

			//create a scanner for it
			try{
			in = new Scanner(file);
			}	
			catch (FileNotFoundException k){
				//the file was not found!
				System.out.println("File could not be opened!");
			}
			
			//read in message
			String name;
			name = in.nextLine();
			for (int k=0; k<length3; k++){
				char a = key.charAt(k);
				int ascii1 = (int)a;
				//put ascii value of letter in key to array
				keyAsciiValues[k]= ascii1;
			}
			//measure length of code message array
			int length1 = name.length();
			//measures length of strings in code message array
			for(int j=0;j<length1;j++){
				char c = name.charAt(j);
				int ascii = (int)c;
				ascii -= keyAsciiValues[count];
				if(c != ' '){
					count++;
				}
				if(count>length3-1){
					count = 0;
				}
				while(ascii<33){
					ascii+= 93;
				}
				char b=(char)ascii;
				if(c == ' '){
					b = ' ';
				}
				name1 += b;
			}
			System.out.print(name1);

        }
        JFrame parentFrame = new JFrame();
   	 
   	 JFileChooser fileChooser = new JFileChooser();
   	 fileChooser.setDialogTitle("Which file would you like to save to?");  
   	 int userSelection = fileChooser.showSaveDialog(parentFrame);
   	  
   	 if (userSelection == JFileChooser.APPROVE_OPTION) {
   		 try {
	            // open the output file
   			 	File fileToSave = fileChooser.getSelectedFile();
	            PrintWriter file = new PrintWriter(fileToSave);

	            // write some numbers to the file
	          
	                file.println(name1);
	            

	            file.close();
	        } catch (FileNotFoundException k) {
	            System.out.println("Error, could not open file to save to");
	        }
   	     
   	 }  
   	 in.close();	  
    } 
    
 
    	 
     
    
    
   
 
    //Must be called from the event dispatch thread.
    protected void resetFocus() {
        passwordField.requestFocusInWindow();
    }
 
    public static Password1 createAndShowGUI() {
    	
    	
        //Create and set up the window.
        JFrame frame = new JFrame("Key");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 
        //Create and set up the content pane.
        final Password1 newContentPane = new Password1(frame);
        newContentPane.setOpaque(true); //content panes must be opaque
        frame.setContentPane(newContentPane);
 
        //Make sure the focus goes to the right component
        //whenever the frame is initially given the focus.
        frame.addWindowListener(new WindowAdapter() {
            public void windowActivated(WindowEvent e) {
                newContentPane.resetFocus();
            }
        });
 
        //Display the window.
        frame.pack();
        frame.setVisible(true);
    return newContentPane;
    } 
 
    public static void main(String[] args) {
        //creating and showing this application's GUI.
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                //Turn off metal's use of bold fonts
        UIManager.put("swing.boldMetal", Boolean.FALSE);
        createAndShowGUI();
            }
        });
    }
}

