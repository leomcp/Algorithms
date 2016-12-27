
package socketprog;
import java.io.*;
import java.net.*;
public class SocketProg {
    public static void main(String[] args) {
        try{
            ServerSocket ssobj=new ServerSocket(6666);
            Socket sobj=ssobj.accept();
            DataInputStream disobj=new DataInputStream(sobj.getInputStream());
            String str=(String)disobj.readUTF();
            System.out.println("Message :"+str);
            ssobj.close();
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }   
}
