package string_java;

//Question 5: Write a Java program to find duplicate characters in a string.

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
//Output:
//     Duplicate characters in the specified string: 
//     r
//     e
//     t
//     s
//     i
