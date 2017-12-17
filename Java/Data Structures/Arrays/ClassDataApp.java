
package Arrays;
////////////////////////////////////////////////////////////////////////////////
public class ClassDataApp {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        int maxSize=100;
        ClassDataArray arr;
        arr=new ClassDataArray(maxSize);
        
        arr.insert("Evans", "Patty", 24);
        arr.insert("Smith", "Lorraine", 37);
        arr.insert("Yee", "Tom", 63);
        arr.insert("Adams", "Henry", 21);
        arr.insert("Hashinoto", "Sato", 21);
        arr.insert("Stimson", "Henry", 29);
        arr.insert("Lamarque", "Henry", 54);
        arr.insert("Vang", "Mint", 22);
        arr.insert("Velasquez", "Jose", 72);
        arr.insert("Creswell", "Lucinda", 18);
        
        arr.displayA();
        
        String searchKey="Stimson";
        Person found;
        found=arr.find(searchKey);
        
        if(found!=null){
            System.out.print("Found ");
            found.displayPerson();
        }
        else
            System.out.println("Can't find "+searchKey);
        
        System.out.println("deleting Vang Velasquez Creswell");
        arr.delete("Vang");
        arr.delete("Velasquez");
        arr.delete("Creswell");
        
        arr.displayA();
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////

/*
OUTPUT 

 Last Name Evans, FIrst Name Patty, Age 24
 Last Name Smith, FIrst Name Lorraine, Age 37
 Last Name Yee, FIrst Name Tom, Age 63
 Last Name Adams, FIrst Name Henry, Age 21
 Last Name Hashinoto, FIrst Name Sato, Age 21
 Last Name Stimson, FIrst Name Henry, Age 29
 Last Name Lamarque, FIrst Name Henry, Age 54
 Last Name Vang, FIrst Name Mint, Age 22
 Last Name Velasquez, FIrst Name Jose, Age 72
 Last Name Creswell, FIrst Name Lucinda, Age 18
Found  Last Name Stimson, FIrst Name Henry, Age 29
deleting Vang Velasquez Creswell
 Last Name Evans, FIrst Name Patty, Age 24
 Last Name Smith, FIrst Name Lorraine, Age 37
 Last Name Yee, FIrst Name Tom, Age 63
 Last Name Adams, FIrst Name Henry, Age 21
 Last Name Hashinoto, FIrst Name Sato, Age 21
 Last Name Stimson, FIrst Name Henry, Age 29
 Last Name Lamarque, FIrst Name Henry, Age 54


*/
