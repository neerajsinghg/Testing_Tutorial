package string_java;

//Question 6: Write a Java program to find the duplicate words in a string.

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
//Output:
//      Duplicate words in the specified string: 
//      love
//      life
//      his