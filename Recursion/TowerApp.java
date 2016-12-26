/*
 Solves the tower of hanoi puzzle 
 */
package Recursion;

public class TowerApp {
    static int nDisks=3;
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        doTowers(nDisks,'A','B','C');
    }
    //--------------------------------------------------------------------------
    public static void doTowers(int topN,char from,char inter,char to){
        if(topN==1)
            System.out.println("Disk 1 from "+from+" to "+to);
        else{
            doTowers(topN-1, from, to, inter);
            System.out.println("Disk "+topN+" from"+from+" to "+to);
            doTowers(topN-1, inter, from, to);
        }
    }
    //--------------------------------------------------------------------------
}
/* OUTPUT
Disk 1 from A to C
Disk 2 fromA to B
Disk 1 from C to B
Disk 3 fromA to C
Disk 1 from B to A
Disk 2 fromB to C
Disk 1 from A to C
*/
