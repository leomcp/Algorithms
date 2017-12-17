/*Linear Search */
package Arrays;
import java.util.Scanner;

public class LinearSearch {
    
     int len,valueToSearch;
     Scanner linearscn=new Scanner(System.in);
     
     //-------------------------------------------------------------------------------------------------------
    LinearSearch(){
        
        System.out.println("*******Linear Search********");
        
        System.out.println("Enter number of elements");
        len=linearscn.nextInt();
        System.out.println("Enter the array elements");
        int thearray[]=new int[len+1];
        for(int i=0;i<len;i++){
            
            thearray[i]=linearscn.nextInt();
        }
        
        System.out.println("Array created. Enter the value to search using linear search :");
        valueToSearch=linearscn.nextInt();
        this.linearSearch(thearray, valueToSearch,len);
        
    }
    
    //-------------------------------------------------------------------------------------------------------
    private void linearSearch(int array[],int value,int len){
        int count=0;
        for(int i=0;i<len;i++){
            if(array[i]==value){
                System.out.println("Element found at "+(i+1)+"th position");
                count++;
            }
        }rohansonawane 
        if(count==0){
            System.out.println("Element Not found !!!");
        }
    }
    //-------------------------------------------------------------------------------------------------------
    public static void main(String args[]){
        LinearSearch lsr=new LinearSearch();
        
    }
}
/* OUTPUT
*******Linear Search********
Enter number of elements
5
Enter the array elements
2
3
5
1
7
Array created. Enter the value to search using linear search :
3
Element found at 2th position
*/
