
package SortedList;

public class SortedListApp {
    public static void main(String args[]){
        SortedList theSortedList=new SortedList();
        theSortedList.insert(20);
        theSortedList.insert(40);
        
        theSortedList.displayList();
        
        theSortedList.insert(10);
        theSortedList.insert(30);
        theSortedList.insert(50);
        
        theSortedList.remove();
        
        theSortedList.displayList();
        
    }
}


/* 
OUTPUT :

List (first-->last):20 40 
List (first-->last):20 30 40 50 
*/