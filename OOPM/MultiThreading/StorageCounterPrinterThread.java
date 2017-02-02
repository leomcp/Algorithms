/*
 
 */
package MultiThreading;
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
public class StorageCounterPrinterThread {
    public static void main(String args[]){
        Storage s=new Storage();
        Counter c=new Counter(s);
        Printer p=new Printer(s);
        new Thread(c,"Counter").start();
        new Thread(p,"Printer").start();
    }
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Storage{
    int i;
    boolean Printed=true;
    //-----------------------------------------------------------------------------------------------------------------------
    public void setValue(int i){
        this.i=i;
    }
    //-----------------------------------------------------------------------------------------------------------------------
    public int getValue(){
        return this.i;
    }
    //-----------------------------------------------------------------------------------------------------------------------
    public boolean isPrinted(){
        return Printed;
    }
    //-----------------------------------------------------------------------------------------------------------------------
    public void setPrinted(boolean p){
        Printed=p;
    }
    //-----------------------------------------------------------------------------------------------------------------------
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Counter extends Thread{
    Storage st;
    //-----------------------------------------------------------------------------------------------------------------------
    Counter(Storage s) {
        st=s;
    }
    //-----------------------------------------------------------------------------------------------------------------------
    public void run(){
        synchronized(st){
              System.out.println("Entering Counter Thread ");
              for(int i=0;i<=10;i++){
                  while(!st.isPrinted()){
                      try{
                          st.wait();
                      }
                      catch(InterruptedException e){
                          e.printStackTrace();
                      }
                  }
              st.setValue(i);
              st.setPrinted(false);
              System.out.println("Thread : "+Thread.currentThread()+" "+st.getValue()+" Printed : "+st.isPrinted());
              st.notify();
           }
        System.out.println("Exiting Counter Thread");
        } 
    }
    //-----------------------------------------------------------------------------------------------------------------------
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Printer extends Thread{
    Storage st;
    //-----------------------------------------------------------------------------------------------------------------------
    Printer(Storage s){
        st=s;
    }
    //-----------------------------------------------------------------------------------------------------------------------
    public void run(){
        synchronized(st){
            System.out.println("Entering Printer Thread");
            for(int i=0;i<=10;i++){
                while(st.isPrinted()){
                    try{
                        st.wait();
                    }catch(InterruptedException e){
                        e.printStackTrace();
                    }
                }
                st.setPrinted(true);
                System.out.println("Thread : "+Thread.currentThread()+" "+st.getValue()+" Printed : "+st.isPrinted());
                st.notify();
            }
            System.out.println("Exiting Printer Thread");
        }
    }
    //-----------------------------------------------------------------------------------------------------------------------
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/*
OUTPUT :

Entering Counter Thread 
Thread : Thread[Counter,5,main] 0 Printed : false
Entering Printer Thread
Thread : Thread[Printer,5,main] 0 Printed : true
Thread : Thread[Counter,5,main] 1 Printed : false
Thread : Thread[Printer,5,main] 1 Printed : true
Thread : Thread[Counter,5,main] 2 Printed : false
Thread : Thread[Printer,5,main] 2 Printed : true
Thread : Thread[Counter,5,main] 3 Printed : false
Thread : Thread[Printer,5,main] 3 Printed : true
Thread : Thread[Counter,5,main] 4 Printed : false
Thread : Thread[Printer,5,main] 4 Printed : true
Thread : Thread[Counter,5,main] 5 Printed : false
Thread : Thread[Printer,5,main] 5 Printed : true
Thread : Thread[Counter,5,main] 6 Printed : false
Thread : Thread[Printer,5,main] 6 Printed : true
Thread : Thread[Counter,5,main] 7 Printed : false
Thread : Thread[Printer,5,main] 7 Printed : true
Thread : Thread[Counter,5,main] 8 Printed : false
Thread : Thread[Printer,5,main] 8 Printed : true
Thread : Thread[Counter,5,main] 9 Printed : false
Thread : Thread[Printer,5,main] 9 Printed : true
Thread : Thread[Counter,5,main] 10 Printed : false
Exiting Counter Thread
Thread : Thread[Printer,5,main] 10 Printed : true
Exiting Printer Thread
*/