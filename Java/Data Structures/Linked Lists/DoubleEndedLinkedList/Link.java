
package DoubleEndedLinkedList;

public class Link {
    public long dData;    // data item
    public Link next;     // next link in list 
    //----------------------------------------------------------
    public Link(long d){   //Constructor
        dData =d;
    }
    //----------------------------------------------------------
    public void displayLink(){       //display this link
        System.out.print(dData+" ");
    }
    //----------------------------------------------------------
}
