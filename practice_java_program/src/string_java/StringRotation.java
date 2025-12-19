package string_java;

//Question 4: Let’s write a Java program to determine whether one string is the rotation of another string.


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
//Output:
//     Second string is rotation of first string.