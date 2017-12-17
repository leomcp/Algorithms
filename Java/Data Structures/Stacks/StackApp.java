
package Stacks;

public class StackApp {
    public static void main(String[] args) {
        // TODO code application logic here
        StackX theStack=new StackX(10);
        theStack.push('A');
        theStack.push('B');
        theStack.push('C');
        theStack.push('D');
        theStack.push('E');
        
        System.out.println("Peek :"+theStack.peek());
        
        while(!theStack.isEmpty()){
            char value=theStack.pop();
            System.out.print(""+value);
            System.out.print(" ");
        }
        System.out.println(""); 
    }
}
