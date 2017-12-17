
package BinaryTree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class TreeApp {
    public static void main(String args[]) throws IOException{
        int value;
        Tree theTree=new Tree();
        
        theTree.insert(50, 1.5);
        theTree.insert(25, 1.2);
        theTree.insert(75, 1.7);
        theTree.insert(12, 1.5);
        theTree.insert(37, 1.2);
        theTree.insert(43, 1.7);
        theTree.insert(30, 1.5);
        theTree.insert(33, 1.2);
        theTree.insert(87, 1.7);
        theTree.insert(93, 1.5);
        theTree.insert(97, 1.5);
        
        while(true){
            System.out.print("Enter first letter of show, ");
            System.out.print("insert, find, delete or traverse : ");
            int choice =getChar();
            switch(choice){
                case 's': theTree.displayTree();
                          break;
                case 'i': System.out.print("Enter value to insert :");
                          value=getInt();
                          theTree.insert(value, value+0.9);
                          break;
                case 'f': System.out.print("Enter value to find :");
                          value =getInt();
                          Node found=theTree.find(value);
                          if(found!=null){
                              System.out.print("Found: ");
                              found.disaplayNode();
                              
                          }
                          else
                              System.out.print("Could not find");
                          System.out.println();
                          break;
                case 'd': System.out.print("Enter value to delete: ");
                          value=getInt();
                          boolean didDelete =theTree.delete(value);
                          if(didDelete)
                              System.out.print("Deleted "+value+'\n');
                          else
                              System.out.println("could not delete");
                          break;
                case 't': System.out.print("Enter type 1,2 or 3: ");
                          value=getInt();
                          theTree.traverse(value);
                          break;
                default: System.out.println("Invalid Entry !!!");          
            }
        }
    }
    //--------------------------------------------------------------------------
    public static String getString()throws IOException{
        InputStreamReader isr=new InputStreamReader(System.in);
        BufferedReader br =new BufferedReader(isr);
        String s=br.readLine();
        return s ;
    }
    //--------------------------------------------------------------------------
    public static char getChar() throws IOException{
        String s=getString();
        return s.charAt(0);
    }
    //--------------------------------------------------------------------------
    public static int getInt() throws IOException{
        String s =getString();
        return Integer.parseInt(s);
    }
    //--------------------------------------------------------------------------
}


/*
OUTPUT :

Enter first letter of show, insert, find, delete or traverse : s
...............................................................
                                50                                                              
                25                              75                              
        12              37              --              87              
    --      --      30      43      --      --      --      93      
  --  --  --  --  --  33  --  --  --  --  --  --  --  --  --  97  
...............................................................
Enter first letter of show, insert, find, delete or traverse : i
Enter value to insert :10
Enter first letter of show, insert, find, delete or traverse : s
...............................................................
                                50                                                              
                25                              75                              
        12              37              --              87              
    10      --      30      43      --      --      --      93      
  --  --  --  --  --  33  --  --  --  --  --  --  --  --  --  97  
...............................................................
Enter first letter of show, insert, find, delete or traverse : f
Enter value to find :97
Found: { 97, 1.5 }
Enter first letter of show, insert, find, delete or traverse : d
Enter value to delete: 33
Deleted 33
Enter first letter of show, insert, find, delete or traverse : s
...............................................................
                                50                                                              
                25                              75                              
        12              37              --              87              
    10      --      30      43      --      --      --      93      
  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  97  
...............................................................
Enter first letter of show, insert, find, delete or traverse : t
Enter type 1,2 or 3: 1

 Preorder Traversal :50 25 12 10 37 30 43 75 87 93 97 
Enter first letter of show, insert, find, delete or traverse : t
Enter type 1,2 or 3: 2

 Inorder Traversal :10 12 25 30 37 43 50 75 87 93 97 
Enter first letter of show, insert, find, delete or traverse : t
Enter type 1,2 or 3: 3

 Postorder Traversal :10 12 30 43 37 25 97 93 87 75 50 
Enter first letter of show, insert, find, delete or traverse : s
...............................................................
                                50                                                              
                25                              75                              
        12              37              --              87              
    10      --      30      43      --      --      --      93      
  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  97  
...............................................................


*/