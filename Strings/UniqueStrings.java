/*
  To implement an algorithms to determine whether given string has unique characters 
  or not.
 */
package Strings;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class UniqueStrings {

    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        System.out.println("Enter a String :");
        String str=getString();
        if(isUniqueString(str))
            System.out.println("Given string has unique characters.");
        else
            System.out.println("Given string doesn't have unique character");
    }
    //--------------------------------------------------------------------------
    public static String getString() throws IOException{
        InputStreamReader isr=new InputStreamReader(System.in);
        BufferedReader br=new BufferedReader(isr);
        String s=br.readLine();
        return s;
    }
    //--------------------------------------------------------------------------
    public static boolean isUniqueString(String str){
        boolean[] char_set=new boolean[256];
        for(int i=0;i<str.length();i++){
            char val=str.charAt(i);
            if(char_set[val])  
                return false;
            char_set[val]=true;
        }
        return true;
    }
    //--------------------------------------------------------------------------
}
