/*
PROBLEM :
The probability that a machine produces a defective product is 1/3. What is the 
probability that the  defect is found during the  inspection?
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
////////////////////////////////////////////////////////////////////////////////
public class GeometricDistribution {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        Scanner scn=new Scanner(System.in);
        int numerator=scn.nextInt();
        int denominator=scn.nextInt();
        int n=scn.nextInt();
        
        double p=(double)numerator/denominator;
        
        System.out.format("%.3f", geometricDistribution(n,p));
    }
    //--------------------------------------------------------------------------
    public static Double geometricDistribution(int n,double p){
        return Math.pow(1-p, n-1)*p;
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT
0.066
*/