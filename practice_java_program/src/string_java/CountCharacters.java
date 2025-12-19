package string_java;

//Question 14: Write a Java program to count the occurrences of each character in string.

public class CountCharacters {
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
  int count = countLetters("String Programs", 'r');
  System.out.println("No of characters: " +count);
 }
}
//Output:
//      No of characters : 2
