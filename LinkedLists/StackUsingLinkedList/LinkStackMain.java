/*
 Demonstrated a stack implemented as a list 
 */
package StackUsingLinkedList;

public class LinkStackMain {
    public static void main(String args[]){
        LinkStack theStack=new LinkStack();
        
        theStack.push(20);
        theStack.push(40);
        
        theStack.displayStack();
        
        theStack.push(60);
        theStack.push(80);
        
        theStack.pop();
        theStack.pop();
        
        theStack.displayStack();
    }
}
/* 
OUTPUT :

Stack(top--->bottom) :
40 20 
Stack(top--->bottom) :
40 20 
*/