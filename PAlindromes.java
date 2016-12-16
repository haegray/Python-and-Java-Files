import java.util.Scanner;
public class PAlindromes
{

    public static boolean Pally(String pally)
    {
        if(pally.length() == 0 || pally.length() == 1)
            return true; 
        if(pally.charAt(0) == pally.charAt(pally.length()-1))
            return Pally(pally.substring(1, pally.length()-1));
        return false;
    
    }
    public static void main(String[]args)
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Is it a Palindrome? (enter word)");
        String pal = in.nextLine();
        if(Pally(pal))
            System.out.println(pal + " is a palindrome");
        else
            System.out.println(pal + " is not a palindrome");
    }
}