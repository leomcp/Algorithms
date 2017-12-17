
package Sorting;



public class Partition {
    public static void main(String args[]){
        int maxSize=16;
        ArrayPr arr;
        arr=new ArrayPr(maxSize);
        
        for(int j=0;j<maxSize;j++){
            long n=(int)(java.lang.Math.random()*99);
            arr.insert(n);
        }
        arr.display();
        
        long pivot=99;
        System.out.print("Pivot is "+pivot);
        int size=arr.size();
        
        int PartDex=arr.partition(0, size-1, pivot);
        
        System.out.println(", Partition is at index "+PartDex);
        arr.display();
        
    }
}
//------------------------------------------------------------------------------
class ArrayPr{
    private long[] theArray;
    private int nElems;
    //--------------------------------------------------------------------------
    ArrayPr(int max){
        theArray=new long[max];
        nElems=0;
    }
    //--------------------------------------------------------------------------
    public void insert(long value){
        theArray[nElems]=value;
        nElems++;
    }
    //--------------------------------------------------------------------------
    public int size(){
        return nElems;
    }
    //--------------------------------------------------------------------------
    public void display(){
        System.out.print("A =");
        for(int i=0;i<nElems;i++)
            System.out.print(theArray[i]+" ");
        System.out.println(" ");
    }
    //--------------------------------------------------------------------------
    public int partition(int left,int right,long pivot){
        int leftPtr=left-1;
        int rightPtr=right-1;
        while(true){
            while(leftPtr<right && theArray[++leftPtr]<pivot); 
            
            while(rightPtr>left && theArray[--rightPtr]>pivot);
            
            if(leftPtr>=rightPtr)
                break;
            else
                swap(leftPtr,rightPtr);
        }
        return leftPtr;
    }
    //--------------------------------------------------------------------------
    public void swap(int dex1,int dex2){
        long temp;
        temp=theArray[dex1];
        theArray[dex1]=theArray[dex2];
        theArray[dex2]=temp;
    }
    //--------------------------------------------------------------------------
}
//------------------------------------------------------------------------------
