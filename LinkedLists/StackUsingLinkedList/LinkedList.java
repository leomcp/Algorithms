
package StackUsingLinkedList;

public class LinkedList {
    private Link first;
    //--------------------------------------------------------------------------
    public LinkedList(){
        first=null;
    }
    //--------------------------------------------------------------------------
    public boolean isEmpty(){
        return first==null;
    }
    //--------------------------------------------------------------------------
    public void insertFirst(long dd){
        Link newLink=new Link(dd);
        newLink.next=first;        //newLink--->old first
        first=newLink;             //first--->newLink
    }
    //--------------------------------------------------------------------------
    public long deleteFirst(){
        Link temp=first;           //save reference to link
        first =first.next;         //delete it; first -->old next 
        return temp.dData;         //return deleted link
    }
    //--------------------------------------------------------------------------
    public void displayList(){
        Link current=first;
        while(current!=null){
            current.displayLink();
            current=current.next;
        }
        System.out.println("");
    }
    //--------------------------------------------------------------------------
}
