/*
 Printing 1 to 10 numbers using Single Thread 
 */
package MultiThreading;
////////////////////////////////////////////////////////////////////////////////
public class Threading extends Thread {
    //--------------------------------------------------------------------------
    public void run(){
        System.out.println("Entering Thread");
        try{
            for(int i=0;i<11;i++){
                Thread.sleep(500);
                System.out.println(" Thread : "+Thread.currentThread()+" "+i);
            }
        }
        catch(InterruptedException e){
            e.printStackTrace();
        }
        finally{
            System.out.println("Exiting thread");
        }
    }
    //--------------------------------------------------------------------------
    public static void main(String[] args) {
        Threading theThread=new Threading();
        theThread.start();
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT :

Entering Thread
 Thread : Thread[Thread-0,5,main] 0
 Thread : Thread[Thread-0,5,main] 1
 Thread : Thread[Thread-0,5,main] 2
 Thread : Thread[Thread-0,5,main] 3
 Thread : Thread[Thread-0,5,main] 4
 Thread : Thread[Thread-0,5,main] 5
 Thread : Thread[Thread-0,5,main] 6
 Thread : Thread[Thread-0,5,main] 7
 Thread : Thread[Thread-0,5,main] 8
 Thread : Thread[Thread-0,5,main] 9
 Thread : Thread[Thread-0,5,main] 10
Exiting thread

*/
