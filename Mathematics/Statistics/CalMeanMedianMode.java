
package Statistics;
////////////////////////////////////////////////////////////////////////////////
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
////////////////////////////////////////////////////////////////////////////////
public class CalMeanMedianMode {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        Scanner scn=new Scanner(System.in);
        System.out.print("Enter number of elements : ");
        int numofElems=scn.nextInt();
        
        OrdArray oa=new OrdArray(numofElems);
        
        System.out.println("Enter array value : ");
        int sum=0;
        for(int i=0;i<numofElems;i++){
            int num=scn.nextInt();
            oa.insert(num);
            sum+=num;
        }
            
        oa.display();
        System.out.println("Mean :"+oa.mean(sum));
        System.out.println("Median : "+oa.median());
        System.out.println("Mode : "+oa.mode());
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
class OrdArray{
    private int a[];
    private int nELems;
    //--------------------------------------------------------------------------
    public OrdArray(int maxSize){
        a=new int[maxSize];
        nELems=0;
    }
    //--------------------------------------------------------------------------
    public int size(){
        return nELems;
    }
    //--------------------------------------------------------------------------
    public void insert(int value){
        int j;
        for(j=0;j<nELems;j++)
            if(a[j]>value)
                break;
        for(int k=nELems;k>j;k--)
            a[k]=a[k-1];
        a[j]=value;
        nELems++;
    }
    //--------------------------------------------------------------------------
    public void display(){
        for(int i=0;i<nELems;i++)
            System.out.print(""+a[i]+" ");
        System.out.println("");
    }
    //--------------------------------------------------------------------------
    public double mean(int sum){
       // System.out.println(""+sum);
        return sum/nELems;
    }
    //--------------------------------------------------------------------------
    public double median(){
        if(nELems%2==0){
            double n=a[nELems/2]+a[(nELems/2)-1];
            //System.out.println(""+n);
            return n/2;
        }
        else{
            return (double)a[nELems/2];
        }
    }
    //--------------------------------------------------------------------------
    public int mode(){
        int mode=a[0];
        int maxFreq=0;
        Map<Integer,Integer> modeMap=new HashMap<Integer, Integer>();
        
        for(int num:a){
            if(modeMap.containsKey(num)){
                int freq=modeMap.get(num)+1;
                modeMap.put(num, freq);
                if(freq>maxFreq){
                   maxFreq=freq;
                   mode=num;
                }     
            }
            else{
                modeMap.put(num,1);
            }
        }
        return mode; 
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
