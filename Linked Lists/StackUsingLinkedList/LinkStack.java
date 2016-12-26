/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package StackUsingLinkedList;

/**
 *
 * @author parab
 */
public class LinkStack {
    private LinkedList theList;
    //--------------------------------------------------------------------------
    public LinkStack(){
        theList=new LinkedList();
    }
    //--------------------------------------------------------------------------
    public void push(long j){
        theList.insertFirst(j);
    }
    //--------------------------------------------------------------------------
    public long pop(){
        return theList.deleteFirst();
    }
    //--------------------------------------------------------------------------
    public boolean isEmpty(){
        return (theList.isEmpty());
    }
    //--------------------------------------------------------------------------
    public void displayStack(){
        System.out.println("Stack(top--->bottom) :");
        theList.displayList();
    }
    //--------------------------------------------------------------------------
}
