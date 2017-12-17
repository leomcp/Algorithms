/*
PROBLEM :
You have a sample of 100 values from a population with mean 500 and with 
standard deviation 80 . Compute the interval that covers the middle 95% of the 
distribution of the sample mean; in other words, compute A and B such that 
P(A<x<B)=0.95. Use the value of z=1.96. 
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
public class CentralLimitTheoremIII {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        double mean   = 500;
        double std    = 80;
        int    n      = 100;
        double zScore = 1.96; 
        
        double marginOfError = zScore * std / Math.sqrt(n);

        System.out.format("%.2f%n", mean - marginOfError);
        System.out.format("%.2f%n", mean + marginOfError);
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT :
484.32
515.68
*/
