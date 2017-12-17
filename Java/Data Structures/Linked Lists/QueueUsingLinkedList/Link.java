
package QueueUsingLinkedList;

public class Link {
    public long dData;  // data item
    public Link next;     // next Link in list
    //----------------------------------------------------------------
    public Link(long dd){
        dData=dd;                     
    }
    //----------------------------------------------------------------
    public void displayLink(){
        System.out.print("{"+dData+", "+dData+"} ");
    }
}
