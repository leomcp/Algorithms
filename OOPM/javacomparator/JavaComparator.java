/*
 Simple program to show use of Comparator to sort the list based on name and age 
 of a student.
 */
package javacomparator;
////////////////////////////////////////////////////////////////////////////////
import java.util.*;
import java.io.*;
////////////////////////////////////////////////////////////////////////////////
public class JavaComparator {
    //--------------------------------------------------------------------------
    public static void main(String[] args) {
        ArrayList<Object> al=new ArrayList<Object>();
        
        al.add(new Student(101,"Saurbh",23));
        al.add(new Student(102,"Sachin",28));
        al.add(new Student(103,"Rahul",20));
        
        System.out.println("Sorting by name .........");
        Collections.sort(al,new NameComparator());
        Iterator itr =al.iterator();
        while(itr.hasNext()){
            Student s=(Student) itr.next();
            System.out.println(s.name+" "+s.rolNo+" "+s.age);
        }
        
        
        System.out.println("Sorting by age ...........");
        Collections.sort(al,new AgeComparator());
        Iterator itr2=al.iterator();
        while(itr2.hasNext()){
            Student s=(Student) itr2.next();
            System.out.println(s.name+" "+s.rolNo+" "+s.age);
        }
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT :
Sorting by name .........
Rahul 103 20
Sachin 102 28
Saurbh 101 23
Sorting by age ...........
Rahul 103 20
Saurbh 101 23
Sachin 102 28
*/