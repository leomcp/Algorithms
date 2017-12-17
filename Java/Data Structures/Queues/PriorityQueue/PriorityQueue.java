
package PriorityQueue;

public class PriorityQueue {
    //array in sorted order, from max at 0 to min at size-1
    private int maxSize;
    private long[] queArray;
    private int nItems;
    //--------------------------------------------------------------------------
    public PriorityQueue(int s){
        maxSize=s;
        queArray =new long[maxSize];
        nItems=0;
    }
    //--------------------------------------------------------------------------
    public void insert(long item){
        int i;
        if(nItems==0)
            queArray[nItems++]=item;
        else{
            for(i=nItems-1;i>=0;i--){
                if(item>queArray[i])
                    queArray[i+1]=queArray[i];
                else
                    break;
            }
            queArray[i+1]=item;
            nItems++;
        }
    }
    //--------------------------------------------------------------------------
    public long remove(){
        return queArray[--nItems];
    }
    //--------------------------------------------------------------------------
    public long peekMin(){
        return queArray[nItems-1];
    }
    //--------------------------------------------------------------------------
    public boolean isEmpty(){
        return (nItems==0);
    }
    //--------------------------------------------------------------------------
    public boolean isFull(){
        return (nItems==maxSize);
    }
    //--------------------------------------------------------------------------
}
