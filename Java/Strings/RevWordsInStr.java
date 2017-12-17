/*
 Program to reverse all words in a string.
 */
package Strings;
////////////////////////////////////////////////////////////////////////////////
public class RevWordsInStr {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        String inputStr="This is a string";
        System.out.println("Input String : "+inputStr);
        
        String[] splitStr=inputStr.split(" ");
        String outputStr="";
        
        for(int i=splitStr.length-1;i>=0;i--)
            outputStr+=splitStr[i]+" ";
        
        System.out.println("Output String : "+outputStr);
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT :
Input String : This is a string
Output String : string a is This 
*/