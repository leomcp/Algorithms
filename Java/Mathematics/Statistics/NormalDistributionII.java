/*
PROBLEM :
The final grades for a Physics exam taken by a large group of students have a 
mean of 70 and a standard deviation of 10. If we can approximate the 
distribution of these grades by a normal distribution, what percentage of
the students:
1. Scored higher than 80 (i.e., have a grade > 80)?
2. Passed the test (i.e., have a grade > 60 )?
3. Failed the test (i.e., have a grade < 60)?
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
public class NormalDistributionII {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        double mean = 70;
        double std  = 10;
            
        System.out.format("%.2f%n", 100 * (1 - commulativeDistFunc(mean, std, 80)));
        System.out.format("%.2f%n", 100 * (1 - commulativeDistFunc(mean, std, 60)));
        System.out.format("%.2f%n", 100 * commulativeDistFunc(mean, std, 60));
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
15.87
84.13
15.87
*/