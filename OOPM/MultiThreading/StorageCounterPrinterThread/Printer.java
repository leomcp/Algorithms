/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package OOPM.Multithreading.StorageCounterPrinterThread;
////////////////////////////////////////////////////////////////////////////////
class Printer implements Runnable{
    Storage st;
    //--------------------------------------------------------------------------
    Printer(Storage s){
        st=s;
    }
    //--------------------------------------------------------------------------
    public void run(){
        synchronized(st){
            for(int i=0;i<=5;i++){
                while(st.isPrinted()){
                    try{
                        st.wait();
                    }catch(Exception e){
                        e.printStackTrace();
                    }
                }
         System.out.println(Thread.currentThread().getName()+" "+st.getValue());
         st.setPrinted(true);
         st.notify();
            }
        }
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////

