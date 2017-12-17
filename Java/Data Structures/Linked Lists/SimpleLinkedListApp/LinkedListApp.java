
package SimpleLinkedListApp;

public class LinkedListApp {

    public static void main(String[] args) {
        // TODO code application logic here
        
        LinkedList theList=new LinkedList();       //make new List
        
        theList.insertFirst(22, 2.99);             //insert four items 
        theList.insertFirst(44, 4.99);
        theList.insertFirst(66, 6.99);
        theList.insertFirst(88, 8.99);
        
        theList.displayList(); 
        
        //Finding a link 
        Link f =theList.find(44);
        if(f!=null)
            System.out.println("Found link with key :"+f.iData);
        else
            System.out.println("Can't find the link");
        
        //Deleting a Link
        Link d=theList.delete(66);
        if(d!=null)
            System.out.println("Deleted link with key "+d.iData);
        else
            System.out.println("Can't delete the link");
        
        //Displaying the List
        theList.displayList();
        
        while(!theList.isEmpty()){
            Link aLink=theList.deleteFirst();      //delete link
            System.out.print("Deleted");           //display it 
            aLink.displayLink();
            System.out.println("");
        }
        theList.displayList();
    }
}

/*

OUTPUT :

List (first-->Last):{88, 8.99} {66, 6.99} {44, 4.99} {22, 2.99} 
Found link with key :44
Deleted link with key 66
List (first-->Last):{88, 8.99} {44, 4.99} {22, 2.99} 
Deleted{88, 8.99} 
Deleted{44, 4.99} 
Deleted{22, 2.99} 
List (first-->Last):
*/