/*
PROBLEM :
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo 
containing 49 boxes must be transported via the elevator. The box weight of this 
type of cargo follows a distribution with a mean of 205 pounds and a 
standard deviation of 15 pounds. Based on this information, what is the 
probability that all 49 boxes can be safely loaded into the freight elevator 
and transported?
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
public class CentralLimitTheoremI {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        double mean=205;
        double std=15;
        double maxWgt=9800;
        int nBox=49;
        
        double sampleMean=nBox*mean;
        double sampleStd=Math.sqrt(nBox)*std;
        
        System.out.format("%.4f", commulativeDistFunc(sampleMean, sampleStd, maxWgt));
    }
    //--------------------------------------------------------------------------
    public static double commulativeDistFunc(double m, double s, double x){
        double parameter=(x-m)/(s*Math.sqrt(2));
        return 0.5*(1+erf(parameter));
    }
    //--------------------------------------------------------------------------
    /* Source: http://introcs.cs.princeton.edu/java/21function/ErrorFunction.java.html */
    // fractional error in math formula less than 1.2 * 10 ^ -7.
    // although subject to catastrophic cancellation when z in very close to 0
    // from Chebyshev fitting formula for erf(z) from Numerical Recipes, 6.2
     public static double erf(double z) {
        double t = 1.0 / (1.0 + 0.5 * Math.abs(z));
        // use Horner's method
        double ans = 1 - t * Math.exp( -z*z   -   1.26551223 +
                                            t * ( 1.00002368 +
                                            t * ( 0.37409196 + 
                                            t * ( 0.09678418 + 
                                            t * (-0.18628806 + 
                                            t * ( 0.27886807 + 
                                            t * (-1.13520398 + 
                                            t * ( 1.48851587 + 
                                            t * (-0.82215223 + 
                                            t * ( 0.17087277))))))))));
        if (z >= 0) return  ans;
        else        return -ans;
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT :
0.010
*/