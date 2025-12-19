package basic_java;

//7. Palindrome
//
//A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.
//
//For example Madam , Mom etc.


public class Palindrome {
    public static void main(String[] args) {
        String original = "mom";
        String reverse = "";
        for (int i = original.length() - 1; i >= 0; i--) {
            reverse += original.charAt(i);
        }
        System.out.println("palindrome or not::" + reverse.equals(original));
    }
}
//output:
//palindrome or not::true