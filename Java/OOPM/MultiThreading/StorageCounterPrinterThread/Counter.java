/*

 */
package OOPM.Multithreading.StorageCounterPrinterThread;
////////////////////////////////////////////////////////////////////////////////
class Counter implements Runnable{
    Storage st;
    //--------------------------------------------------------------------------
    Counter(Storage s){
        st=s;
    }
    //--------------------------------------------------------------------------
    public void run() {
        synchronized(st){
            for(int i=0;i<=5;i++){
                 while(!st.isPrinted()){
                    try{
                        st.wait();
                    }
                    catch(Exception e ){
                        e.printStackTrace();
                    }
                }
                st.setValue(i);
                st.setPrinted(true);
                st.notify();
            }
        }
    }
}
////////////////////////////////////////////////////////////////////////////////
