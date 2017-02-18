/*
 
 */
package OOPM.Multithreading.StorageCounterPrinterThread;
////////////////////////////////////////////////////////////////////////////////
public class StorageCounterPrinterThread {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        Storage s=new Storage();
        Counter c=new Counter(s);
        Printer p=new Printer(s);
        new Thread(c,"Counter").start();
        new Thread(c,"Printer").start();
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
