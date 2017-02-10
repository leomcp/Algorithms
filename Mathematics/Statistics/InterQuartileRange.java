
package Statistics;
////////////////////////////////////////////////////////////////////////////////
import com.sun.xml.internal.fastinfoset.util.ValueArray;
import java.util.Scanner;
////////////////////////////////////////////////////////////////////////////////
public class InterQuartileRange {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        Scanner scn=new Scanner(System.in);
        //System.out.print("Enter number of elements : ");
        int maxSize=scn.nextInt();
        
        int valArray[]=new int[maxSize];
        int freqArray[]=new int[maxSize];
        
        //System.out.println("Enter elements :");
        for(int i=0;i<maxSize;i++)
            valArray[i]=scn.nextInt();
        
        int totalSize=0;
        //System.out.println("Enter their frequencies : ");
        for(int i=0;i<maxSize;i++){
            freqArray[i]=scn.nextInt();
            totalSize+=freqArray[i];
        }
        
        
        //System.out.println("Total size : "+totalSize);
        
        OrdIQRArray oiqr=new OrdIQRArray(totalSize);
        
        for(int i=0;i<maxSize;i++)
            for(int j=0;j<freqArray[i];j++){
               // System.out.print("("+i+", "+j+")");
                oiqr.insert(valArray[i]);
            }
                
        //System.out.println("");
                
                
        
        oiqr.display();
        
        double Q1=0.0;
       int Q2=0;
       double  Q3=0.0;
       
       if(oiqr.size()%2==0){
           Q1=oiqr.calMedian(0,totalSize/2-1);
           Q2=((oiqr.getElem(totalSize/2))+(oiqr.getElem((totalSize/2)-1)))/2;
           Q3=oiqr.calMedian(totalSize/2, totalSize-1);
       }
       else{
           Q1=oiqr.calMedian(0,totalSize/2-1);
           Q2=oiqr.getElem((totalSize/2));
           Q3=oiqr.calMedian(totalSize/2+1, totalSize-1);
       }
       
       //System.out.println("[ Q1 : "+Q1+", Q2 : "+Q2+", Q3 : "+Q3+" ]");
       //System.out.println("Inter Quartile range : "+(Q3-Q1));
        System.out.println(""+(Q3-Q1));
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
class OrdIQRArray{
    private int a[];
    private int nELems;
    //--------------------------------------------------------------------------
    public OrdIQRArray(int maxSize) {
        a=new int[maxSize];
        nELems=0;
    }
    //--------------------------------------------------------------------------
    public int size(){
        return nELems;
    }
    //--------------------------------------------------------------------------
    public int getElem(int index){
        return a[index];
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
       // System.out.println("start : "+start+", end "+end);
        int diff=(end-start)+1;
        //System.out.println("diff "+diff);
        if(diff%2==0)
            return (a[(start+(diff/2))]+a[(start+(diff/2)-1)])/2;
        else
            return a[start+(diff/2)];
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
