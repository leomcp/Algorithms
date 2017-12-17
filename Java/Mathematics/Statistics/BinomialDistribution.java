/*
PROBLEM : 
The ratio of boys to girls for babies born in Russia is . If there is  child 
born per birth, what proportion of Russian families with exactly  children will
have at least  boys?

Write a program to compute the answer using the above parameters.
Then print your result, rounded to a scale of  decimal places (i.e.,  format).
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
public class BinomialDistribution {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        double ratio=1.09;
        double p=ratio/(ratio+1);
        int n=6;
        
        double result=0;
        for(int x=3;x<=n;x++){
            result=result+binomial(x,n,p);
        }
        System.out.format("%.3f", result);
    }
    //--------------------------------------------------------------------------
    public static Double binomial(int x,int n, double p){
        if(p<0 || p>1 || n<0 || x<0 || x>n){
            return null;
        }
        return combinations(n,x)*Math.pow(p, x)*Math.pow(1-p, n-x);
    }
    //--------------------------------------------------------------------------
    private static Long combinations(int n,int x){
        if(x<0 || n<0 || x>n){
            return null;
        }
        return factorial(n)/(factorial(x)*factorial(n-x));
    }
    //--------------------------------------------------------------------------
    private static Long factorial(int a){
        if(a<0){
            return null;
        }
        long result=1;
        while(a>0){
            result*=a--;
        }
        return result;
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT :
0.696
*/