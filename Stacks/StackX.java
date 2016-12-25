
package Stacks;
import java.io.*;

public class StackX {
    private int maxSize;
    private char[] stackArray;
    private int top;
    //--------------------------------------------------------------------------
    //constructor
    public StackX(int s){
        maxSize=s;
        stackArray=new char[maxSize];
        top=-1;
    }
    //--------------------------------------------------------------------------
    //push items on stack
    public void push(char j){
        stackArray[++top]=j;
        //put item on top pf stack
        //increment top and then insert 
    }
    //--------------------------------------------------------------------------
    //pop item from stack
    public char pop(){
        return stackArray[top--];
    }
    //--------------------------------------------------------------------------
    //take item feom the top
    //acess item and decrement the top
    //Find peek
    public char peek(){
        return stackArray[top];
    }
    //--------------------------------------------------------------------------
    //True if it empty 
    public boolean isEmpty(){
        return (top==-1);
    }
    //--------------------------------------------------------------------------
    //Check if stack is full
    public boolean isFull(){
        return (top==maxSize-1);
    }
    //--------------------------------------------------------------------------
}
