package Heaps;
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
////////////////////////////////////////////////////////////////////////////////
public class HeapSortApp {
    //--------------------------------------------------------------------------
    public static void main(String args[]) throws IOException {
        int size, j;
        System.out.print("Enter the number of items : ");
        size = getInt();
        Heap theHeap = new Heap(size);

        for (j = 0; j < size; j++) {
            int random = (int) (java.lang.Math.random() * 100);
            Node newNode = new Node(random);
            theHeap.insertAT(j, newNode);
            theHeap.incrementSize();
        }

        System.out.print("Random: ");
        theHeap.displayArray();

        for (j = size / 2 - 1; j >= 0; j--) {
            theHeap.trickleDown(j);
        }

        System.out.print("Heap : ");
        theHeap.displayArray();
        theHeap.displayHeap();

        for (j = size - 1; j >= 0; j--) {
            Node biggestNode = theHeap.remove();
            theHeap.insertAT(j, biggestNode);
        }

        System.out.print("Sorted : ");
        theHeap.displayArray();
    }
    //--------------------------------------------------------------------------
    public static String getString() throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        String s = br.readLine();
        return s;
    }
    //--------------------------------------------------------------------------
    public static int getInt() throws IOException {
        String s = getString();
        return Integer.parseInt(s);
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

/*
OUTPUT
Enter the number of items : 10
Random: 89 83 90 51 15 26 16 36 73 8  
Heap : 90 83 89 73 15 26 16 36 51 8  
Heap Array : 90 83 89 73 15 26 16 36 51 8 
................................................................................
                                90
                83                              89
        73              15              26              16
    36      51      8
................................................................................
Sorted : 8 15 16 26 36 51 73 83 89 90  
*/