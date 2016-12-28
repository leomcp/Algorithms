/*
 To implement algorithm to remove all dublicate characters from a given string.
 */
package Strings;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class RemoveDuplicates {
    
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        System.out.println("Enter a String :");
        String str=getString();
        char char_set[]= str.toCharArray();
        removeDuplicates(char_set);
    }
    //--------------------------------------------------------------------------
    public static String getString() throws IOException{
        InputStreamReader isr=new InputStreamReader(System.in);
        BufferedReader br=new BufferedReader(isr);
        String s=br.readLine();
        return s;
    }
    //--------------------------------------------------------------------------
    public static void removeDuplicates(char[] str){
        if(str==null) return;
        int len=str.length;
        if(len<2) return;
        
        int tail=1;
        
        for(int i=1;i<len;++i){
            int j;
            for(j=1;j<tail;++j){
                if(str[i]==str[j]) break;
            }
            if(j==tail){
                str[tail]=str[i];
                ++tail;
            }
        }
        str[tail]=0;
        String updatedStr=String.valueOf(str);
        System.out.println("String after removal of duplicate character : "+updatedStr);
    }
    //--------------------------------------------------------------------------
}
