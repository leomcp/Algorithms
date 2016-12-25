
package SimpleLinkedListApp;

public class LinkedList {
   private Link first;          //ref to first link on List
   
   //----------------------------------------------------------------
   public LinkedList(){         // Constructor 
       first=null;
   }
   //----------------------------------------------------------------
   public boolean isEmpty(){
       return (first==null);    
   }
   //----------------------------------------------------------------
   public void insertFirst(int id,double dd){
       Link newLink =new Link(id,dd);         //newLink --> old first 
       newLink.next=first;                    //first --> newLink
       first=newLink;
   }
   //----------------------------------------------------------------
   public Link deleteFirst(){                 //delete first item
       Link temp=first;                       //save reference ot link 
       first =first.next;                     //delete it : first -->old next
       return temp;                           //return deleted link 
   }
   //----------------------------------------------------------------
   public void displayList(){
       System.out.print("List (first-->Last):");
       Link current =first ;              //start at begining of list 
       while (current !=null){
           current.displayLink();        //print data 
           current=current.next;         // move to next link
       }
       System.out.println("");
   }
   //----------------------------------------------------------------
   public Link find(int key){           //Find link with given key 
       Link current=first ;            //Start at first 
       while (current.iData!=key){     //while no match
           if(current.next==null)   
               return null;        //if end of list , did'nt got link
           else
               current=current.next;
       }      
       return current;
   }
   //----------------------------------------------------------------
   public Link delete(int key){           //Delete the key with given key 
       Link current =first ;              //search foe the link
       Link previous=first;
       while (current.iData!=key){
           if(current.next==null)
               return null;            //did'nt fint it
           else{
               previous=current;      //got to next link
               current=current.next ;
           }
       }                              //found it 
       if(current==first)             //if first link
           first=first.next;          //change first 
       else
           previous.next=current.next;
       return current;   
   }
 //----------------------------------------------------------------  
}
