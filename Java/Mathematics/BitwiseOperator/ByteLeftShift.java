/*
 Left Shifting a byte value 
 */
package BitwiseOperator;

public class ByteLeftShift {
    public static void main(String args[]){
        byte a=64, b;
        int i;
        
        i=a<<2;
        b=(byte) (a<<2);
        
        System.out.println("Original value of a : "+a);
        System.out.println("i and b "+i+" "+b);
    }
}
/*
OUTPUT
Original value of a : 64
i and b 256 0
*/
