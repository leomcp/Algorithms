
package Statistics;
////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
////////////////////////////////////////////////////////////////////////////////
public class WeightedMean {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        Scanner scn=new Scanner(System.in);
        int nElems=scn.nextInt();
        int xArray[]=new int[nElems];
        int wArray[]=new int [nElems];
        
        for(int i=0;i<nElems;i++){
            xArray[i]=scn.nextInt();
        }
        
        double sumwArray=0;
        for(int i=0;i<nElems;i++){
            wArray[i]=scn.nextInt();
            sumwArray=sumwArray+wArray[i];
        }
        
        double weightedSum=0;
        for(int i=0;i<nElems;i++)
            weightedSum=weightedSum+(xArray[i]*wArray[i]);
        
        System.out.println("ws"+weightedSum);
        System.out.println("sum"+sumwArray);
        double weightedMean=(weightedSum/sumwArray);
        System.out.printf("%.1f",weightedMean);
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
