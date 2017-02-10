
package Statistics;
////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
////////////////////////////////////////////////////////////////////////////////
public class StandardDeviation {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
       Scanner scn=new Scanner(System.in); 
       int nElems=scn.nextInt();
       
       int eleArray[]=new int[nElems];
       
       int sum=0;
       for(int i=0;i<nElems;i++){
           eleArray[i]=scn.nextInt();
           sum+=eleArray[i];
       }
       
       double mean=(double)sum/nElems;
       
       double sumSd=0.0;
       for(int i=0;i<nElems;i++)
           sumSd=sumSd+Math.pow((eleArray[i]-mean), 2);
       
       double standardDeviation=sumSd/nElems;
       double answer =Math.sqrt(standardDeviation);
       System.out.println(Math.round(answer*10.0)/10.0);
           
    }
    //--------------------------------------------------------------------------
}
