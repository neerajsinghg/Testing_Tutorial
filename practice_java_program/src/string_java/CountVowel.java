package string_java;

//Question 2: Write Java program to count the number of vowels present in a string.

public class CountVowel {
	public static void main(String[] args) 
	{
		String s = "This is my pen";
		//Call toCharArray() method of String class to convert string into char array.	
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
//Output:
//   Enter a string: 
//   Union
//   Number of vowels in the string: 3
//Algorithm:
//
//a. Take a string input from user and store it in a variable called “s”.
//
//b. Convert string to char array using toCharArray() method of String class.
//
//c. Use for loop from i = 0 to i < s.length().
//
//d. Check the following conditions using if statement: s.charAt(i)==’a’ or s.charAt(i)==’e’ or s.charAt(i)==’i’ or s.charAt(i)==’o’ or s.charAt(i)==’o’ to increment vowel++.
//

