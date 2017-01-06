
package Arrays;

public class ArrayApp {
    public static void main(String args[]){
        int maxSize=20;
        long[] arr;
        arr=new long[maxSize];
        int nElems=0;
        int j;
        long searchKey;
        //----------------------------------------------------------------------
        System.out.print("A = ");
        for(int i=0;i<maxSize;i++){
            long n=(int)(java.lang.Math.random()*99);
            arr[i]=n;
            System.out.print(arr[i]+" ");
        }
        System.out.println(" ");
        //----------------------------------------------------------------------
        searchKey=66;
        for(j=0;j<nElems;j++)
            if(arr[j]==searchKey)
                break;
        if(j==nElems)
            System.out.println("Can't find "+ searchKey);
        else
            System.out.println("Found "+ searchKey);
        //----------------------------------------------------------------------
        System.out.print("A = ");
        for(j=0;j<nElems;j++)
            System.out.print(arr[j]+" ");
        System.out.println("");
        //----------------------------------------------------------------------
    }
}
//------------------------------------------------------------------------------
