
package Heaps;
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.nio.Buffer;
////////////////////////////////////////////////////////////////////////////////
public class HeapApp {
    public static void main(String args[]) throws IOException{
        int value,value2;
        Heap theHeap=new Heap(31);
        boolean success;
        
        theHeap.insert(70);
        theHeap.insert(40);
        theHeap.insert(50);
        theHeap.insert(20);
        theHeap.insert(60);
        theHeap.insert(100);
        theHeap.insert(80);
        theHeap.insert(30);
        theHeap.insert(10);
        theHeap.insert(90);
        
        while(true){
            System.out.println("Enter first letter of ");
            System.out.print("Show, insert, remove, change : ");
            int choice =getChar();
            switch(choice){
                case 's':
                    theHeap.displayHeap();
                    break;
                case 'i':
                    System.out.print("Enter value to insert : ");
                    value =getInt();
                    success=theHeap.insert(value);
                    if(!success)
                        System.out.println("Can't insert; heap full");
                    break;
                case 'r':
                    if(!theHeap.isEmpty())
                        theHeap.remove();
                    else
                        System.out.println("Can't remove; heap empty");
                    break;
                case 'c':
                    System.out.print("Enter current index of item : ");
                    value=getInt();
                    System.out.println("Enter new Key : ");
                    value2=getInt();
                    success=theHeap.change(value, value2);
                    if(!success)
                        System.out.println("Invalid index");
                    break;
                default:
                    System.out.println("Invalid entry\n");
            }
        }
    }
    //--------------------------------------------------------------------------
    public static String getString() throws IOException{
        InputStreamReader isr=new InputStreamReader(System.in);
        BufferedReader br=new BufferedReader(isr);
        String s=br.readLine();
        return s;
    }
    //--------------------------------------------------------------------------
    public static char getChar() throws IOException{
        String s=getString();
        return s.charAt(0);
    }
    //--------------------------------------------------------------------------
    public static int getInt() throws IOException{
        String s=getString();
        return Integer.parseInt(s);
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

/*
OUTPUT 

run:
Enter first letter of 
Show, insert, remove, change : s
Heap Array : 100 90 80 30 60 50 70 20 10 40 
................................................................................
                                100
                90                              80
        30              60              50              70
    20      10      40
................................................................................
Enter first letter of 
Show, insert, remove, change : i
Enter value to insert : 53
Enter first letter of 
Show, insert, remove, change : s
Heap Array : 100 90 80 30 60 50 70 20 10 40 53 
................................................................................
                                100
                90                              80
        30              60              50              70
    20      10      40      53
................................................................................
Enter first letter of 
Show, insert, remove, change : r
Enter first letter of 
Show, insert, remove, change : s
Heap Array : 90 60 80 30 53 50 70 20 10 40 
................................................................................
                                90
                60                              80
        30              53              50              70
    20      10      40
................................................................................
Enter first letter of 
Show, insert, remove, change : 


*/
