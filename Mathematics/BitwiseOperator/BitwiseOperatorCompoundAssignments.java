
package BitwiseOperator;

public class BitwiseOperatorCompoundAssignments {
    public static void main(String args[]){
        int a=1;
        int b=2;
        int c=3;
        
        a<<=2;
        b|=4;
        c>>=1;
        
        System.out.println("a : "+a+"  b : "+b+"  c : "+c);
    }
}
/*OUTPUT
a : 4  b : 6  c : 1
*/