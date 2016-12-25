
package Stacks;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ReverseString {
    private String input;
    private String output;
    //--------------------------------------------------------------------------
    public ReverseString(String in){
        input=in;
    }
    //--------------------------------------------------------------------------
    public String doRev(){
        int stackSize=input.length();
        StackX theStack=new StackX(stackSize);
        
        for(int j=0;j<input.length();j++){
            char ch=input.charAt(j);
            theStack.push(ch);
        }
        output=" ";
        while(!theStack.isEmpty()){
            char ch= theStack.pop();
            output=output+ch;
        }
        return output;
    }
    //--------------------------------------------------------------------------
    public static String getString()throws IOException{
        InputStreamReader isr=new InputStreamReader(System.in);
        BufferedReader br=new BufferedReader(isr);
        String s =br.readLine();
        return s;        
    }
    //--------------------------------------------------------------------------
    public static void main(String args[])throws IOException{
        String input,output;
        
            System.out.print("Enter a String :");
            System.out.flush();
            input=getString();
            if(!input.equals("")){
            ReverseString theReverser=new ReverseString(input);
            output=theReverser.doRev();
            System.out.println("Reversed String :"+output);
            }
    }
}

/*
OUTPUT :

Enter a String :String java
Reversed String : avaj gnirtS
*/
