/*
 --------------Double Ended List-------------------
A double ended list is similar to an ordinary linked list, but 
it has one additional feature: a reference to the last link as 
well as to first. The reference to the last link permits you to
insert a new link directly at the end of list as well as at the 
beginning, makes it suitable for certain situations tha a single
ended list can't handle it efficiently.
 */
package DoubleEndedLinkedList;

public class DoubleEndedListApp {
    public static void main(String args[]){
        DoubleEndedList theList=new DoubleEndedList();
        
        //insert at front 
        theList.insertFirst(22);
        theList.insertFirst(44);
        theList.insertFirst(66);
        
        //insert at rear 
        theList.insertLast(11);
        theList.insertLast(33);
        theList.insertLast(55);
        
        //Display the list 
        theList.displayList();
        
        //delete first two items 
        theList.deleteFirst();
        theList.deleteFirst();
        
        //Display list again,
        theList.displayList();
    }
}

/* 
OUTPUT 
List (first-->last):66 44 22 11 33 55 
List (first-->last):22 11 33 55 
*/