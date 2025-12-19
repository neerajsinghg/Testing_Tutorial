package basic_java;

//Print if the strings are Anagram or not?
//An anagram is a word or phrase that’s formed by rearranging the letters of another word or phrase.

import java.util.Arrays;

public class Anagram {
 public static void main(String[] args) {
     String str1 = "own";
     String str2 = "now";
     char[] chArray1 = str1.toCharArray();
     char[] chArray2 = str2.toCharArray();
     Arrays.sort(chArray1);
     Arrays.sort(chArray2);
     System.out.println(Arrays.equals(chArray1, chArray2));
 }
}