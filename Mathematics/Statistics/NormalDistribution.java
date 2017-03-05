/*
PROBLEM :
In a certain plant, the time taken to assemble a car is a random variable, X, 
having a normal distribution with a mean of 20 hours and a standard deviation 
of 2 hours. 
What is the probability that a car can be assembled at this plant in:
1. Less than 19.5 hrs?
2. Between 20 and 22hrs?
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
public class NormalDistribution {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        double mean=20;
        double std=2;
        System.out.format("%.3f%n",commulativeDistFunc(mean, std, 19.5));
        System.out.format("%.3f%n",(commulativeDistFunc(mean, std, 22)
                - commulativeDistFunc(mean, std, 20)));
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
0.401
0.341
*/