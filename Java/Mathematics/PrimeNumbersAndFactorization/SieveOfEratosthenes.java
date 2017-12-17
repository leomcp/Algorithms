/*
 Printing all prime numbers from 1 to given n.
 */
package PrimeNumbersAndFactorization;

import java.util.Scanner;

public class SieveOfEratosthenes {
        //--------------------------------------------------------------------------
    public static void main(String args[]){
        Scanner scn =new Scanner(System.in);
        System.out.print("Enter a number : ");
        int num=scn.nextInt();
        sieveOfEratosthenes(num);
    }
    //--------------------------------------------------------------------------
    private static void sieveOfEratosthenes(int num){
        boolean prime[]=new boolean[num+1];
        for(int i=0;i<num;i++)
            prime[i]=true;
        
           for(int p = 2; p*p <=num; p++)
        {
            // If prime[p] is not changed, then it is a prime
            if(prime[p] == true)
            {
                // Update all multiples of p
                for(int i = p*2; i <= num; i += p)
                    prime[i] = false;
            }
        }
         
        // Print all prime numbers
        for(int i = 2; i <= num; i++)
        {
            if(prime[i] == true)
                System.out.print(i + " ");
        }
    }
    //--------------------------------------------------------------------------
}
/*
OUTPUT
Enter a number : 50
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
*/