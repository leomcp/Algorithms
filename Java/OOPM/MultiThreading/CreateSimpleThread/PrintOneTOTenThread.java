/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package OOPM.Multithreading.CreateSimpleThread;
//////////////////////////////////////////////////////////////////////////////////////////////////////
import java.util.logging.Level;
import java.util.logging.Logger;
///////////////////////////////////////////////////////////////////////////////////////////////////////
public class PrintOneTOTenThread implements Runnable {
    //-------------------------------------------------------------------------------------------------
    public static void main(String args[]){
        PrintOneTOTenThread p=new PrintOneTOTenThread();
    }
    Thread t;
    //-------------------------------------------------------------------------------------------------
    public PrintOneTOTenThread() {
        t=new Thread();
        t.start();
    }
    //-------------------------------------------------------------------------------------------------
    public void run() {
        for(int i=0;i<=10;i++){
            System.out.println(" "+i);
            try {
                t.sleep(1000);
            } catch (InterruptedException ex) {
                Logger.getLogger(PrintOneTOTenThread.class.getName()).log(Level.SEVERE, null, ex);
                ex.printStackTrace();
            }
        }
    }
    //-------------------------------------------------------------------------------------------------
}
