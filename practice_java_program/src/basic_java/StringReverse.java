package basic_java;

//11. Reverse a string ( word or a sentence) iterative/recursive way.

public class StringReverse {
    public static void main(String[] args) {
        //Reverse a word
        String word = "Hello";
        for (int i = word.toCharArray().length - 1; i >= 0; i--) {
            System.out.print(word.toCharArray()[i]);
        }

        //reverse a sentence
        String str = "Hello today is expiry";
        String[] arr = str.split(" ");
        String result = "";
        for (int i = arr.length - 1; i >= 0; i--) {
            result += arr[i] + " ";
        }
        System.out.println("\n" + result);

        System.out.println("\nUsing recursion");
        reverse(word);


    }

    // recursion to reverse a sentence
    static void reverse(String str) {
        if ((str == null) || (str.length() <= 1))
            System.out.println(str);
        else {
            System.out.print(str.charAt(str.length() - 1));
            reverse(str.substring(0, str.length() - 1));
        }
    }

}
//output :
//olleH
//expiry is today Hello 
//
//Using recursion
//olleH