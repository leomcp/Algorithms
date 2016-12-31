/*
 To check whether given number is prime or not
 */
package PrimeNumbersAndFactorization;

import java.util.Scanner;

public class IsPrime {
    //--------------------------------------------------------------------------
    public static void main(String[] args) {
        Scanner scn =new Scanner(System.in);
        System.out.print("Enter a Number to check : ");
        int num=scn.nextInt();
        if(isPrime(num)){
            System.out.println(num+" is a prime number.");
        }
        else{
            System.out.println(num+" is not a prime number.");
        }
    }
    //--------------------------------------------------------------------------
    public static boolean isPrime(int num){
        //corner cases
        if(num<=2) return false;
        if(num<=3) return true;
        
        if(num%2==0 || num%3==0) return false;
        
        for(int i=5;i*i<=num;i+=6){
            if(num%i==0 || num%(i+2)==0)
                return false;
        }
        return true;
    }
    //--------------------------------------------------------------------------
}

/* 
OUTPUT 
Enter a Number to check : 11
11 is a prime number.
*/
