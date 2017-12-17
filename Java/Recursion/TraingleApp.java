
package Recursion;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class TraingleApp {
    static int theNumber;
    //--------------------------------------------------------------------------
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        System.out.print("Enter a number : ");
        theNumber=getInt();
        int theAnswer=traingle(theNumber);
        System.out.println("Traingle = "+theAnswer);
    }
    //--------------------------------------------------------------------------
    public static int traingle(int n){
        if(n==1)
            return 1;
        else
            return (n+traingle(n-1));
    }
    //--------------------------------------------------------------------------
    public static String getString() throws IOException{
        InputStreamReader isr=new InputStreamReader(System.in);
        BufferedReader br=new BufferedReader(isr);
        String s=br.readLine();
        return s;
    }
    //--------------------------------------------------------------------------
    public static int getInt() throws IOException{
        String s =getString();
        return Integer.parseInt(s);
    }
    //--------------------------------------------------------------------------
}
/* OUYPUT
Enter a number : 10
Traingle = 55
*/