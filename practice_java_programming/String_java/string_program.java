Question 1: Write a Java program to count the total number of characters present in a string.

To count the number of characters present in the given string, we will iterate through the string and count the number of characters. Look at the program code below.

Program code:

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
JAVA
Copy code
Output:
     Total number of characters in a string: 26
In this example, we have used charAt() method of String class. Basically, the charAt() method returns the char value at the specified index. An index ranges from 0 to length() – 1. The first char value is at index 0, the next at index 1,and so on.

Question 2: Write Java program to count the number of vowels present in a string.

Program code:

import java.util.Scanner;
public class CountVowels {
public static void main(String[] args) 
{
// Create a Scanner class object to accept input from keyword.	
   Scanner sc = new Scanner(System.in);
// Prompt the user to enter a string.   
	System.out.println("Enter a string: ");
	String s = sc.nextLine();
// Call toCharArray() method of String class to convert string into char array.	
   char[ ] ch = s.toCharArray();
	int vowel = 0;
	
  for (int i = 0; i < s.length(); i++) 
  { 
   if(s.charAt(i)=='a' || s.charAt(i)=='A' || s.charAt(i)=='e' || s.charAt(i)=='E' 
   || s.charAt(i)=='i' || s.charAt(i)=='I' || s.charAt(i)=='o' || s.charAt(i) == 'O' 
   || s.charAt(i)=='u' || s.charAt(i) == 'U') 
   vowel++; 
  }
  System.out.println("Number of vowels in the string: " + vowel);   	
 }
}
JAVA
Copy code
Output:
     Enter a string: 
     Union
     Number of vowels in the string: 3
Algorithm:

a. Take a string input from user and store it in a variable called “s”.

b. Convert string to char array using toCharArray() method of String class.

c. Use for loop from i = 0 to i < s.length().

d. Check the following conditions using if statement: s.charAt(i)==’a’ or s.charAt(i)==’e’ or s.charAt(i)==’i’ or s.charAt(i)==’o’ or s.charAt(i)==’o’ to increment vowel++.


Question 3: Write a Java program to count the number of words present in a string.

There are three ways to count the number of words present in a string. Let’s see all three methods in the below program one by one.

Program code:

public class WordCount {
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
JAVA
Copy code
Output:
     Number of words in a string = 4
     Number of words in a string = 2
     Number of words in a string = 5

Question 4: Let’s write a Java program to determine whether one string is the rotation of another string.

Program code:

public class StringRotation {
public static void main(String[] args) 
{
   String st1 = "abcde";
   String st2 = "deabc";
   if(st1.length() != st2.length())
   {
      System.out.println("Second string is not rotation of first string.");	 
   }
   else {
  // Concatenate st1 with st1 and store it in st1.
     st1 = st1.concat(st1);
  // Check whether st2 is present in st1.
     if(st1.indexOf(st2) != -1)
	System.out.println("Second string is rotation of first string.");
     else
	System.out.println("Second string is not rotation of first string.");	 
   }
  }
}
JAVA
Copy code
Output:
     Second string is rotation of first string.
Question 5: Write a Java program to find duplicate characters in a string.

Program code:

public class DuplicateCharacter {
public static void main(String[] args) 
{
   String str = "Great responsibility";
   int count = 0;
// Converting given string into character array.
   char[] ch = str.toCharArray();
   System.out.println("Duplicate characters in the specified string: ");
// Counting each character present in a string.
   for(int i = 0; i < ch.length; i++)
   {
     count = 1;
     for(int j = i + 1; j < ch.length; j++) 
     { 
       if((ch[i] == ch[j]) && (ch[i] != ' ')) { 
          count++; 
       // Setting ch[j] to 0 to avoid printing visited character. 
          ch[j] = '0'; 
       } 
     } 
  // If count is greater than 1 then consider character as duplicate. 
     if(count > 1 && ch[i] != '0')
        System.out.println(ch[i]);	
     }
   }
}
JAVA
Copy code
Output:
     Duplicate characters in the specified string: 
     r
     e
     t
     s
     i
Question 6: Write a Java program to find the duplicate words in a string.

Program code:

public class DuplicateWords {
public static void main(String[] args) 
{
   String str = "Love life love his life his";
   int count = 0;
 // Converts string into lowercase.
    str = str.toLowerCase();
// Now splits the string into words using split() method of String class.
   String[] words = str.split(" ");
    System.out.println("Duplicate words in the specified string: ");
// Counting each word present in a string.
   for(int i = 0; i < words.length; i++)
   {
     count = 1;
     for(int j = i + 1; j < words.length; j++) 
     { 
        if(words[i].equals(words[j])) { 
          count++; 
       // Setting words[j] to 0 to avoid printing visited word. 
          words[j] = "0"; 
        } 
     } 
  // If count is greater than 1 then consider a word as duplicate. 
     if(count > 1 && words[i] != "0")
        System.out.println(words[i]);	
    }
  }
}
JAVA
Copy code
Output:
      Duplicate words in the specified string: 
      love
      life
      his
Question 7: Write a Java program to find whether a string is palindrome.

Go to this tutorial for best explanation: String Palindrome in Java

Question 8: Write a program to check whether a number is palindrome.

Refer to this tutorial for best explanation: Palindrome number in Java

Question 9: Write a program to reverse a string in Java.

Go to this tutorial for best explanation: How to reverse a string in Java

Question 10: Write a program to separate individual characters from a string.

Program code:

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
JAVA
Copy code
Output:
     Individual characters from string: 
     T e c h n o l o g y 
Question 11: Write a Java program to sort an array of strings in alphabetical order.

Refer to this tutorial for best practice: How to Sort String in Java Alphabetically

Question 12: Write a Java program to determine the frequency of characters in the String.

Program code:

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
JAVA
Copy code
Output:
      Frequency of character e = 5


      Question 13: Write a Java program to count the number of lines, words, and characters in a text file.

Program code:

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class CountWords {
public static void main(String[] args) throws IOException 
{
  int nl = 0, nw = 0, nc = 0;
  String line;
  FileReader fr = new FileReader("D:\\textfile.txt");
  BufferedReader br = new BufferedReader(fr);
  while((line = br.readLine()) != null)
  {
    nl++;
    nc += line.length();
    StringTokenizer st = new StringTokenizer(line);
    nw += st.countTokens();
  }
  System.out.printf("Number of lines: \t %d", nl);
  System.out.printf("\nNumber of words: \t %d", nw);
  System.out.printf("\nNumber of characters: \t %d", nc);
 }
}
JAVA
Copy code
Output:
     Number of lines:	 2
     Number of words:	 9
     Number of characters: 37
Question 14: Write a Java program to count the occurrences of each character in string.

Program code:

public class CountCharacter {
static int countLetters(String str, char ch) 
{
  if (str == null || str.length() == 0) {
    return 0;
  }
// Convert all letters into lowercase.  
   String s = str.toLowerCase();
   int count = 0;
   for (int i = 0; i < s.length(); i++) 
   {
      if (ch == s.charAt(i)) 
      {
	count++;
      }
    }
    return count;
  }	
public static void main(String[] args)
{
  int count = countLetters("String Programs", 's');
  System.out.println("No of characters: " +count);
 }
}
JAVA
Copy code
Output:
      No of characters : 2
We can also find the number of occurrences of a character in a string using Java 8 streams and lambdas, and regular expressions. Let’s write simple code for it.

Program code:

import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class CountCharacter 
{
// Using Java 8 streams and lambdas	
  static long countOccurrencesOf(String str, char character) 
  {
    String lowercase = str.toLowerCase();	
    return lowercase.codePoints().filter(ch -> ch == character).count();
  }	
// Using regular expressions.
   static long countCharsUsingReg(String str, char character) 
   {
     String lowercase = str.toLowerCase();   
     Pattern pattern = Pattern.compile("[^" + character + "]*" + character + "");
     Matcher matcher = pattern.matcher(lowercase);
     int count = 0;
     while (matcher.find()) {
         count++;
      }
      return count;
   }
public static void main(String[] args)
{
  long count = countOccurrencesOf("String Programs", 's');
  System.out.println("No of characters: " +count);
  long count2 = countCharsUsingReg("String programs", 's');
  System.out.println("Number of characters: " +count2);
 }
}
JAVA
Copy code
Output:
      No of characters: 2
      Number of characters: 2
Question 15: Write a Java program to check two strings are anagram or not.

Refer to this tutorial for the best practice: Anagram in Java | How to Check it.