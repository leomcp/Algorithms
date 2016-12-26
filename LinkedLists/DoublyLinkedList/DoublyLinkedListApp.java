/*
 Demonstrates Double Linked List 
 */
package DoublyLinkedList;

public class DoublyLinkedListApp {
    public static void main(String args[]){
        DoublyLinkedList theList=new DoublyLinkedList();
        
        theList.insertFirst(22);
        theList.insertFirst(44);
        theList.insertFirst(66);
        
        theList.insertLast(11);
        theList.insertLast(33);
        theList.insertLast(55);
        
        theList.displayForward();
        theList.displayBackwards();
        
        theList.deleteFirst();
        theList.deleteLast();
        theList.deleteKey(11);
        
        theList.insertAfter(22,77);
        theList.insertAfter(33,88);
        
        theList.displayForward();
                
    }
}
/*
OUTPUT:
(first-->last):
66 44 22 11 33 55 
List(last-->first):55 33 11 22 44 66 
(first-->last):
44 22 77 11 33 88 
*/