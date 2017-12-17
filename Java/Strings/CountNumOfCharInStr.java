
package Strings;

import java.util.HashMap;
import java.util.Map;

public class CountNumOfCharInStr {
    public static void main(String args[]){
        String str="Hello World";
        int len=str.length();
        
        Map<Character,Integer> numChar=new HashMap<Character,Integer>();
        for(int i=0;i<len;i++){
            char charAt=str.charAt(i);
            if(!numChar.containsKey(charAt)){
                numChar.put(charAt, 1);
            }
            else{
                numChar.put(charAt, numChar.get(charAt)+1);
            }
        }
        System.out.println(numChar);
    }
}
