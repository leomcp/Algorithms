/*
 Program to check the given string is a palindrome or not.
 */
package Strings;
////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
////////////////////////////////////////////////////////////////////////////////
public class IsStrPalindrome {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        Scanner scn=new Scanner(System.in);
        
        System.out.println("Enter a String to check if it is palindrome ");
        String orgStr=scn.nextLine();
        
        String revStr="";
        for(int i=orgStr.length()-1;i>=0;i--)
            revStr+=orgStr.charAt(i);
        
        if(revStr.equals(orgStr))
            System.out.println(orgStr+" is a palindrome");
        else
            System.out.println(orgStr+" is not a palindrome");
        
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT : 
Enter a String to check if it is palindrome 
madam
madam is a palindrome
*/