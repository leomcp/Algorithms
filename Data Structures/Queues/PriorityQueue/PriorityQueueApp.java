
package PriorityQueue;

import sun.security.pkcs11.P11TlsKeyMaterialGenerator;

public class PriorityQueueApp {
    public static void main(String args[]){
        PriorityQueue thePQ=new PriorityQueue(5);
        
        thePQ.insert(30);
        thePQ.insert(50);
        thePQ.insert(10);
        thePQ.insert(40);
        thePQ.insert(20);
        
        System.out.println("PriorityQueue: ");
        while(!thePQ.isEmpty()){
            long item=thePQ.remove();
            System.out.print(item+" ");
        }
        System.out.println("");
    }
}
