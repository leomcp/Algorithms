
package SimpleLinkedListApp;

public class Link {
    public int iData;     //Data item (key)
    public double dData;  // data item
    public Link next;     // next Link in list
    
    //----------------------------------------------------------------
    public Link(int id,double dd){
        iData=id;                     //initialize data
        dData=dd;                     //('next' is automatically set to null)
    }
    //----------------------------------------------------------------
    public void displayLink(){
        System.out.print("{"+iData+", "+dData+"} ");
    }
}//end class Link
