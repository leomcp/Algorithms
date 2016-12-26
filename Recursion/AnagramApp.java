
package Recursion;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class AnagramApp {
    static int size;
    static int count;
    static char[] arrChar=new char[100];
    //--------------------------------------------------------------------------
    public static void main(String args[]) throws IOException{
        System.out.println("Enter a word");
        String input=getString();
        size=input.length();
        count=0;
        for(int j=0;j<size;j++)
            arrChar[j]=input.charAt(j);
        doAnagram(size);
    }
    //--------------------------------------------------------------------------
    public static void doAnagram(int newSize){
        if(newSize==1)
            return;
        for(int j=0;j<newSize;j++){
            doAnagram(newSize-1);
            if(newSize==2);
                 displayWord();
            rotate(newSize);
        }
    }
    //--------------------------------------------------------------------------
    public static void rotate(int newSize){
        int j;
        int position=size-newSize;
        char temp=arrChar[position];
        for(j=position+1;j<size;j++)
            arrChar[j-1]=arrChar[j];
        arrChar[j-1]=temp;
    }
    //--------------------------------------------------------------------------
    public static void displayWord(){
        if(count<99)
            System.out.print(" ");
        if(count<9)
            System.out.print(" ");
        System.out.print(++count+" ");
        for(int j=0;j<size;j++)
            System.out.print(arrChar[j]);
        System.out.print("  ");
        System.out.flush();
        if(count%6==0)
            System.out.println("");
    }
    //--------------------------------------------------------------------------
    public static String getString() throws IOException{
        InputStreamReader isr =new InputStreamReader(System.in);
        BufferedReader br=new BufferedReader(isr);
        String s =br.readLine();
        return s ;
    }
    //--------------------------------------------------------------------------
}
/* 
OUTPUT 
Enter a word
cats
  1 cats    2 cast    3 cats    4 ctsa    5 ctas    6 ctsa  
  7 csat    8 csta    9 csat   10 cats   11 atsc   12 atcs  
 13 atsc   14 asct   15 astc   16 asct   17 acts   18 acst  
 19 acts   20 atsc   21 tsca   22 tsac   23 tsca   24 tcas  
 25 tcsa   26 tcas   27 tasc   28 tacs   29 tasc   30 tsca  
 31 scat   32 scta   33 scat   34 satc   35 sact   36 satc  
 37 stca   38 stac   39 stca   40 scat  
*/