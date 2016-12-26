public class InsertSortApp {
    
        public static void main(String args[]){
        
        int maxSize=100;    //array size
        ArrayIns arr =new ArrayIns(maxSize);
        
        arr.insert(77);
        arr.insert(90);
        arr.insert(44);
        arr.insert(55);
        arr.insert(22);
        arr.insert(88);
        arr.insert(11);
        arr.insert(00);
        arr.insert(66);
        arr.insert(33);
        
        arr.display();
        
        arr.insertionSort();
        
        arr.display();
        
    }// end of main()

    
    
}


class ArrayIns{
    private long[] a; // reference to array a 
    private int nElems; //number of data items 
    
    //-------------------------------
    
    public ArrayIns(int max){
        a=new long[max];
        nElems=0;
    }
    
    //-------------------------------
    
    public void insert(long value){  // put element into array 
        a[nElems]=value;
        nElems++;
    }
    
    //--------------------------------
    
    public void display(){       //display array contents
        for(int j=0;j<nElems;j++){
            System.out.print(a[j]+" "); 
        }
        System.out.println();
    }
    
    //------------------------------------------
    
    public void insertionSort(){  
        int out, in;
        
        for(out=1;out<nElems;out++)     //out is  dividing line 
        {
            long temp=a[out];           //remove marked item
            in=out;                     //start shifts at out 
            while(in>0 && a[in-1]>=temp)  //until one is smaller,
            {
                a[in]=a[in-1];          //shifts item to right
                --in;                   // go left one position
            }
            a[in]=temp;
        }// end for  
    }// end SelectionSort()
    
} // end of ArrayBub

