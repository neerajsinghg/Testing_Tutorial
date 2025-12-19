package string_java;

//Question 10: Write a program to separate individual characters from a string.

public class IndividualCharacter {
public static void main(String[] args) 
{
   String str = "Technology";
// Prints individual characters from given string.
   System.out.println("Individual characters from string: ");
// Iterate through string and print individual characters.
   for(int i = 0; i < str.length(); i++)
   {
     System.out.print(str.charAt(i)+ " ");  
   }
 }
}
//Output:
//     Individual characters from string: 
//     T e c h n o l o g y 