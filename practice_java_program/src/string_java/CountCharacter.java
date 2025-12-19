package string_java;
//Question 1: Write a Java program to count the total number of characters present in a string.
//To count the number of characters present in the given string, we will iterate through the string and count the number of characters. Look at the program code below.

public class CountCharacter {
public static void main(String[] args) 
{
// Creating a string.	
   String string = "Every person loves his country"; 
// Set the count zero.   
   int count = 0;    
// Counts each character except space.   
   for(int i = 0; i < string.length(); i++) {    
     if(string.charAt(i) != ' ')    
       count++;    
    }    
// Prints the total number of characters present in the given string.    
   System.out.println("Total number of characters present in a string: " + count);   	
 }
}
//Output:
//     Total number of characters in a string: 26
//In this example, we have used charAt() method of String class. Basically, the charAt() method returns the char value at the specified index. An index ranges from 0 to length() – 1. The first char value is at index 0, the next at index 1,and so on.

