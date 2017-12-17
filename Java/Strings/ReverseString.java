
package Strings;

public class ReverseString {
    public static void main(String args[]){
        String str="Strings";
        String new_str="";
        char str_Array[]=str.toCharArray();
        for(int i=str_Array.length-1;i>=0;i--){
            new_str=new_str+str_Array[i];
        }
        System.out.println("Reverse string of String is "+new_str);
    }
}
//------------------------------------------------------------------------------
/*
OUTPUT
Reverse string of String is sgnirtS
*/