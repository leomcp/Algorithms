
package socketprog;
import java.io.*;
import java.net.*;
public class MyClient {
    public static void main(String args[]){
        try{
        Socket s=new Socket("localhost",6666);
        DataOutputStream dosobj=new DataOutputStream(s.getOutputStream());
        dosobj.writeUTF("Hello Server");
        dosobj.flush();
        dosobj.close();
        s.close();
    }
        catch(Exception e){
            e.printStackTrace();
        }
    }
}

