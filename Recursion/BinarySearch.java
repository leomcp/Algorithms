
package Recursion;

public class BinarySearch {
    public static void main(String args[]){
        int maxSize=100;
        Array arr;
        arr=new Array(maxSize);
        
        arr.insert(72);
        arr.insert(90);
        arr.insert(45);
        arr.insert(72);
        arr.insert(126);
        arr.insert(54);
        arr.insert(99);
        arr.insert(144);
        arr.insert(27);
        arr.insert(125);
        arr.insert(82);
        arr.insert(22);
        
        arr.display();
        
        int searchKey=27;
        if(arr.find(searchKey)!=arr.size())
            System.out.println("Found "+searchKey);
        else
            System.out.println("Can't find "+searchKey);
    }
}
////////////////////////////////////////////////////////////////////////////////
class Array{
    private long[] a;
    private int nElems;
    //--------------------------------------------------------------------------
    public Array(int max){
        a=new long[max];
        nElems=0;
    }
    //--------------------------------------------------------------------------
    public int size(){
        return nElems;
    }
    //--------------------------------------------------------------------------
    public int find(long searchKey){
        return recFind(searchKey,0,nElems-1);
    }
    //--------------------------------------------------------------------------
    private int recFind(long searchKey,int lowerBound, int upperBound){
        int curIn;
        curIn=(lowerBound+upperBound)/2;
        if(a[curIn]==searchKey)
            return curIn;
        else
        {
            if(a[curIn]<searchKey)
                return recFind(searchKey, curIn+1, upperBound);
            else
                return recFind(searchKey, lowerBound, curIn-1);
        }
    }
    //--------------------------------------------------------------------------
    public void insert(long value){
        int j;
        for(j=0;j<nElems;j++)
            if(a[j]>value)
                break;
        for(int k=nElems;k>j;k--)
            a[k]=a[k-1];
        a[j]=value;
        nElems++;
    }
    //--------------------------------------------------------------------------
    public void display(){
        for(int j=0;j<nElems;j++)
            System.out.print(a[j]+" ");
        System.out.println("");
    }
    //--------------------------------------------------------------------------
}


/*
OUTPUT :
22 27 45 54 72 72 82 90 99 125 126 144 
Found 27
*/