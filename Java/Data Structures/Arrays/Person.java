
package Arrays;
////////////////////////////////////////////////////////////////////////////////
public class Person {
    private String lasName;
    private String firstName;
    private int age;
    //--------------------------------------------------------------------------
    public Person(String last,String first,int a){
        lasName=last;
        firstName=first;
        age=a;
    }
    //--------------------------------------------------------------------------
    public void displayPerson(){
        System.out.print(" Last Name "+lasName);
        System.out.print(", FIrst Name "+firstName);
        System.out.print(", Age "+age);
        System.out.println("");
    }
    //--------------------------------------------------------------------------
    public String getLast(){
        return lasName;
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
