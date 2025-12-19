package string_java;

//Question 12: Write a Java program to determine the frequency of characters in the String.

public class FrequencyOfCharacter {
public static void main(String[] args) 
{
  String str = "Welcome to Scientech Easy";
  String lowerCase = str.toLowerCase();
  char ch = 'e';
  int frequency = 0;
  for(int i = 0; i < lowerCase.length(); i++) 
  {
     if(ch == lowerCase.charAt(i)) {
       ++frequency;
     }
  }
  System.out.println("Frequency of character " + ch + " = " + frequency);  
 }
}
//Output:
//      Frequency of character e = 5

