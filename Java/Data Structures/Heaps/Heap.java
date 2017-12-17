/*
Heaps:
  A heap is a binary tree with following characteristics:
    1. It's completely filled in, reading from left to right across each row.
       Although last row need not be full.
    2. It's (usually) implemented in an array.
    3. Each node in a heap satisfy heap condition, which states that every node's
       key is larger than (or equal to) the keys of its children.
    4. Heap is a kind of tree, it offers both insertion and deletion in O(logN)
       time.
Example of Heap :
................................................................................
                                100
                90                              80
        30              60              50              70
    20      10      40
................................................................................

Heaps are mostly used to implement priority queues.

Weakly Ordered :
    1. A heap is weakly ordered compared to binary search tree. Traversing the 
       node in order is difficult because organizing principle is not strong as
       the organizing principle in tree.
    2. Because Heaps are weakly ordered some of the operations are difficult or
       impossible. Heaps does not allow convenient searching for a specified
       key. Hence, Node with specified key can't be deleted in O(logN) time.
       These operations are carried out by O(N) time.
    3. The ordering is sufficient to allow fast removal of the maximum node and 
       fast insertion of new nodes. These operations are needed to use heaps as
       a priority queue.

Removal : Removal means removing the node with maximum key (root node). The root 
is always at index 0 od the heap array.
maxNode=heapArray[0];
Steps for rmoving the maximum node :
    1. Remove the root 
    2. Move the last node into the root
    3. Trickle the last node down until it's below a larger node and above a 
       smaller one.
    4. Removal decreases the array soze by 1.

Insertion : Insertion uses trickle up. Initially, the node to be inserted is 
placed in the first open position at the end of the array, increasing the array 
size by one:
heapArray[N]=newNode;
N++;
These will destroy the heap condition, then trickle up algorithm is used to 
satisfy the condition using appropriate swaping.
*/
package Heaps;
////////////////////////////////////////////////////////////////////////////////
public class Heap {
    private Node[] heapArray;
    private int maxSize;
    private int currentSize;
    //--------------------------------------------------------------------------
    public Heap(int mx){
        maxSize=mx;
        currentSize=0;
        heapArray=new Node[maxSize];
    }
    //--------------------------------------------------------------------------
    public boolean isEmpty(){
        return currentSize==0;
    }
    //--------------------------------------------------------------------------
    public boolean insert(int key){
        if(currentSize==maxSize)            //if array id full,
            return false;                   //Failure
        Node newNode =new Node(key);        //make a newNode 
        heapArray[currentSize]=newNode;     //put it at the end
        trickleUp(currentSize++);           // trickle it up
        return true;                        //success
    }
    //--------------------------------------------------------------------------
    /*`1. find the parent of the index position, and save the node in a variable 
          bottom. 
       2. Inside the while loop the variable index will trickle up the 
          path towards the root, pointing to each node in turn.
       3. loop runs as long as we haven't reached the root and the key index's
          parent is less than the new node.
    */
    public void trickleUp(int index){
        int parent=(index-1)/2;
        Node bottom=heapArray[index];
        while(index>0 && 
                heapArray[parent].getKey()<bottom.getKey()){
            heapArray[index]=heapArray[parent];     //move node down
            index=parent;                           //move index up
            parent=(parent-1)/2;                    //parent<- it's parent 
        }
        heapArray[index]=bottom;
    }
    //--------------------------------------------------------------------------
    public Node remove(){
        Node root=heapArray[0];
        heapArray[0]=heapArray[--currentSize];
        trickleDown(0);
        return root;
    }
    //--------------------------------------------------------------------------
    public void trickleDown(int index){
        int largerChild;
        Node top=heapArray[index];
        while(index<currentSize/2){
            int leftChild=2*index+1;
            int rightChild=leftChild+1;
            
            if(rightChild<currentSize &&
                    heapArray[leftChild].getKey()<
                    heapArray[rightChild].getKey())
                largerChild=rightChild;
            else
                largerChild=leftChild;
            
            if(top.getKey()>=heapArray[largerChild].getKey())
                break;
            
            heapArray[index]=heapArray[largerChild];
            index=largerChild;
        }
        heapArray[index]=top;
    }
    //--------------------------------------------------------------------------
    public boolean change(int index,int newValue){
        if(index<0 || index>=currentSize)
            return false;
        int oldValue=heapArray[index].getKey();
        heapArray[index].setKey(newValue);
        
        if(oldValue<newValue)
            trickleUp(index);
        else
            trickleDown(index);
        return true;
    }
    //--------------------------------------------------------------------------
    public void displayHeap(){
        System.out.print("Heap Array : ");
        for(int m=0;m<currentSize;m++)
            if(heapArray[m]!=null)
                System.out.print(heapArray[m].getKey()+" ");
            else
                System.out.print("--");
        System.out.println("");
        
        int nBlanks=32;
        int itemPerRow=1;
        int column=0;
        int j=0;
        String dots="..............................................";
        System.out.println(dots+dots);
        
        while(currentSize>0){
            if(column ==0 )
                for(int k=0;k<nBlanks;k++)
                    System.out.print(" ");
            
            System.out.print(heapArray[j].getKey());
            
            if(++j==currentSize)
                break;
            
            if(++column==itemPerRow){
                nBlanks/=2;
                itemPerRow*=2;
                column=0;
                System.out.println();
            }
            else
                for(int k=0;k<nBlanks*2-2;k++)
                    System.out.print(" ");
        }
        System.out.println('\n'+dots+dots);
    }
    //--------------------------------------------------------------------------
    public void displayArray(){
        for(int j=0;j<maxSize;j++)
            System.out.print(heapArray[j].getKey()+" ");
        System.out.println(" ");
    }
    //--------------------------------------------------------------------------
    public void insertAT(int index,Node newNode){
        heapArray[index]=newNode;
    }
    //--------------------------------------------------------------------------
    public void incrementSize(){
        currentSize++;
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////