
package QueueUsingLinkedList;

public class DoubleEndedList {
    private Link first;        //ref to first link
    private Link last;         //ref to last link
    //--------------------------------------------------------------------------
    public DoubleEndedList(){    //Constructor 
        first=null;
        last=null;               //no link to list yet 
    }
    //--------------------------------------------------------------------------
    public boolean isEmpty(){    //true if no link
        return first==null;
    }
    //--------------------------------------------------------------------------
    public void insertLast(long dd){     //insert at end of list 
        Link newLink=new Link(dd);        //make a new link
        
        if(isEmpty()){                   //if empty list 
            first= newLink;                //first---->newLink 
        }
        last.next = newLink;            //old last ----------> newLink
        last = newLink;                 //newLink<-----last
    }
    //--------------------------------------------------------------------------
    public long deleteFirst(){            //delete first link
        long temp=first.dData;
        if(first.next==null)
            last=null;
        first=first.next;
        return temp;
    }
    //----------------------------------------------------------
    public void displayList(){
        
        Link current=first;    //start at the beginning
        while(current!=null){  //untill end of list 
            current.displayLink(); //print Data
            current=current.next;  //move to next link
        }
        System.out.println("");
    }
    //----------------------------------------------------------
}

