
package Statistics;
////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
////////////////////////////////////////////////////////////////////////////////
public class Quartiles {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        Scanner scn = new Scanner(System.in);
        
        System.out.print("Enter the number of elements : ");
        int maxSize=scn.nextInt();
        OrdQArray oqa=new OrdQArray(maxSize);
        
        System.out.println("Enter array elements :");
        for(int i=0;i<maxSize;i++){
            int num=scn.nextInt();
            oqa.insert(num);
        }
        
       oqa.display();
       int Q1=0;
       int Q2=0;
       int Q3=0;
       
       if(oqa.size()%2==0){
           Q1=oqa.calMedian(0,maxSize/2-1);
           Q2=oqa.calMedian(0, maxSize-1);
           Q3=oqa.calMedian(maxSize/2, maxSize-1);
       }
       else{
           Q1=oqa.calMedian(0,maxSize/2-1);
           Q2=oqa.calMedian(0, maxSize-1);
           Q3=oqa.calMedian(maxSize/2+1, maxSize-1);
       }
       
       System.out.println("[ Q1 : "+Q1+", Q2 : "+Q2+", Q3 : "+Q3+" ]");
       
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
class OrdQArray{
    private int a[];
    private int nELems;
    //--------------------------------------------------------------------------
    public OrdQArray(int maxSize){
        a=new int[maxSize];
        nELems=0;
    }
    //--------------------------------------------------------------------------
    public int size(){
        return nELems;
    }
    //--------------------------------------------------------------------------
    public void insert(int value){
        int i;
        for(i=0;i<nELems;i++)
            if(a[i]>value)
                break;
        for(int k=nELems;k>i;k--)
            a[k]=a[k-1];
        a[i]=value;
        nELems++;
    }
    //--------------------------------------------------------------------------
    public void display(){
        for(int i=0;i<nELems;i++)
            System.out.print(a[i]+" ");
        System.out.println("");
    }
    //--------------------------------------------------------------------------
    public int calMedian(int start,int end){
        System.out.println("start : "+start+", end "+end);
        int diff=(end-start)+1;
        System.out.println("diff "+diff);
        if(diff%2==0)
            return (a[(start+(diff/2))]+a[(start+(diff/2)-1)])/2;
        else
            return a[start+(diff/2)];
    }
    //--------------------------------------------------------------------------
    public int getElem(int index){
        return a[index];
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////