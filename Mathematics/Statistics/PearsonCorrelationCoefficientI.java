/*
PROBLEM :
Given two n-element data sets, X and Y, 
calculate the value of the Pearson correlation coefficient.
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
////////////////////////////////////////////////////////////////////////////////
public class PearsonCorrelationCoefficientI {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        Scanner scn =new Scanner(System.in);
        
        int maxSize=scn.nextInt();
        double xElems[]=new double[maxSize];
        double yElems[]=new double[maxSize];
        
        for(int i=0;i<maxSize;i++)
            xElems[i]=scn.nextDouble();
        
        for(int i=0;i<maxSize;i++)
            yElems[i]=scn.nextDouble();
        
        System.out.println(pearsonCorrCoff(xElems,yElems));
    }
    //--------------------------------------------------------------------------
    public static double pearsonCorrCoff(double x[],double y[]){
        return (covXY(x, y)/(x.length*calStdDeviation(x)*calStdDeviation(y)));
    }
    //--------------------------------------------------------------------------
    public static Double covXY(double x[],double y[]){
        if(x==null || y==null || x.length!=y.length)
            return null;
        
        double xMean=calMean(x);
        double yMean=calMean(y);
        double cov=0.0;
        for(int i=0;i<x.length;i++)
            cov+=((x[i]-xMean)*(y[i]-yMean));
        
        return cov;
    }
    //--------------------------------------------------------------------------
    public static Double calMean(double arr[]){
        if(arr ==null){
            return null;
        }
        double sum=0;
        for(double elem:arr)
            sum+=elem;
        return sum/arr.length;
    }
    //--------------------------------------------------------------------------
    public static Double calStdDeviation(double arr[]){
        if(arr==null)
            return null;
        
        double sum=0.0;
        double mean=calMean(arr);
        for(double elem:arr)
            sum+=Math.pow((elem-mean), 2);
        return Math.sqrt((sum/arr.length));
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT :
10
10 9.8 8 7.8 7.7 7 6 5 4 2
200 44 32 24 22 17 15 12 8 4
0.6124721937208479
*/