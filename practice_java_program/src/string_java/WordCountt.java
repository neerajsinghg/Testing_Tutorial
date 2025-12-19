package string_java;

//Question 3: Write a Java program to count the number of words present in a string.
//
//There are three ways to count the number of words present in a string. Let’s see all three methods in the below program one by one.

public class WordCountt {
public static void main(String[] args) 
{
// Calling static methods one by one.	
   m1();
   m2();
   m3();
 }
// Method 1 to count the number of words present in a string.
 private static void m1() 
 {
   final String str = "I Love Java Programming!";
   String[ ] strArray = str.split(" "); // Splitting the input string with space.
   System.out.println("Number of words in a string = " + strArray.length);
 }
// Method 2 to count the number of words present in a string.
 private static void m2() 
 {
   final String str = "Java Technology";
   int count = 0;
   for (String word : str.split(" ")) 
    System.out.println(word);
   {
     count++; // It will count the number of words present in the string array.
   }
   System.out.println("Number of words in a string = " + count);
  }
// Method 3 to count the number of words present in a string.
 private static void m3() 
 {
  final String str = "Every people loves his country.";
  int count = 1;
  for (int i = 0; i < str.length() - 1; i++) 
  {
    if ((str.charAt(i) == ' ') && (str.charAt(i + 1) != ' ')) {
    count++;
  }
 }
  System.out.println("Number of words in a string = " +count); 	
 }
}
//Output:
//     Number of words in a string = 4
//     Number of words in a string = 2
//     Number of words in a string = 5
