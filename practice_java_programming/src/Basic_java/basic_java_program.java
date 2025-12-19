// Print if the strings are Anagram or not?
// An anagram is a word or phrase that’s formed by rearranging the letters of another word or phrase.

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
output:
true
2. Array Rotation

Rotate the array clockwise and anticlockwise by no of positions.

package com.commonlyasked;

import java.util.Arrays;

public class ArrayRotation {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int num = 2;
        leftRotation(arr,num);
        rightRotation(arr, num);
    }

    private static void leftRotation(int[] arr, int num) {
        for (int i = 0; i < num; i++) {
            int temp = arr[0];
            for (int j = 0; j < arr.length - 1; j++) {
                arr[j] = arr[j + 1];
            }
            arr[arr.length - 1] = temp;
        }
        System.out.println("Input Array After Left Rotation By " + num +
         " Positions :");

        System.out.println(Arrays.toString(arr));
    }

    private static void rightRotation(int[] arr, int num) {
        for (int i = 0; i < num; i++) {
            int temp = arr[arr.length - 1];
            for (int j = arr.length - 1; j > 0; j--) {
                arr[j] = arr[j - 1];
            }
            arr[0] = temp;
        }
        System.out.println("Input Array After Right Rotation By " + num + 
        " Positions :");

        System.out.println(Arrays.toString(arr));
    }
}
output: 
Input Array After Left Rotation By 2 Positions :
[3, 4, 5, 6, 7, 1, 2]
Input Array After Right Rotation By 2 Positions :
[1, 2, 3, 4, 5, 6, 7]
3. Count the no of 1’s without using any inbuilt function.

package com.commonlyasked;

public class CountOfos1sWithoutInBuilt {
    public static void main(String[] args) {
        int[] arr = new int[]{1, 1, 0, 1, 0, 1, 1, 0};
        int sum = 0;
        for (int i : arr) {
            sum += i;
        }
        System.out.println("count of 1's::" + sum);
        System.out.println("count of 0's::" + (arr.length - sum));

    }
}
output: 
count of 1's::5
count of 0's::3
4. Count the no of ways to reach the nth stair.

There are n stairs, a person standing at the bottom wants to climb stairs to reach the nth stair. The person can climb either 1 stair or 2 stairs at a time, the task is to count the number of ways that a person can reach at the top.

package com.commonlyasked;

/*
In the above approach it can be seen that dp[i] only depends on previous states.
We can optimize the space complexity of the dynamic programming solution to O(1) by using only two variables prev1 and prev2
to keep track of the previous two values of dp[i-1] and dp[i-2]. Since we only need these two values to calculate the next value,
 we don’t need to store the entire array.
Time Complexity: O(N)
Auxiliary Space: O(1)
 */
public class CountWayToReachNStair {
    static int countWays(int n) {
        // declaring  two variables to store the count
        int prev = 1;
        int prev2 = 1;
        // Running for loop to count all possible ways
        for (int i = 2; i <= n; i++) {
            int curr = prev + prev2;
            prev2 = prev;
            prev = curr;
        }
        return prev;
    }

    public static void main(String[] args) {
        int n = 5;
        System.out.println("Number of Ways : "
                + countWays(n));

    }
}

output:  
Number of Ways : 8
5. Factorial of a number recursively/ iterative way

The factorial of a whole number is the function that multiplies the number by every natural number below it.

n! or “n factorial” means:

n! = 1 · 2 · 3 · … · n = Product of the first n positive integers = n(n-1)(n-2)…………………….(3)(2)(1)
Example: 5 factorial, that is, 5! can be written as: 5! = 5 × 4 × 3 × 2 × 1 = 120.

package com.commonlyasked;

public class Factorial {

    // Recursion way
    static int fact(int num) {
        if (num < 0) return -1;
        if (num == 0) return 1;
        else
            return (num * fact(num - 1));

    }

    public static void main(String[] args) {
        //Iterative way
        int fact = 1;
        int num = 5;
        if (num < 0) System.out.println("Factorial cant be calculated for
        negative no");
        if (num == 0) System.out.println("Factorial of 0 is::" + 1);
        for (int i = 1; i <= num; i++) {
            fact = fact * i;
        }
        System.out.println("Factorial of " + num + " using iterative way " 
        + fact);

        System.out.println("Factorial of " + num + " using recursive way " 
        + fact(num));
    }
}
output :
Factorial of 5 using iterative way 120
Factorial of 5 using recursive way 120 
6. Fibonacci of a number

The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers

Get Veenarao’s stories in your inbox
Join Medium for free to get updates from this writer.

Enter your email
Subscribe
Using this numbering, the Fibonacci sequence can be defined by the following three equations:

F0 = 0 (applies only to the first integer)
F1 = 1 (applies only to the second integer)
Fn = Fn-1 + Fn-2 (applies to all other integers)
package com.commonlyasked;

public class Fibonacci {
    //recursion
    public static int fibonaci(int num) {
        if (num < 0) return 0;
        if (num == 1 || num == 2) return 1;
        else
            return fibonaci(num - 2) + fibonaci(num - 1);
    }

    public static void main(String[] args) {

        //iterative way
        int num = 5;
        int n1;
        int n2 = 0, n3 = 1;
        System.out.println("Fibonaci series using iteration::");
        for (int i = 0; i < num; i++) {
            n1 = n2;
            n2 = n3;
            n3 = n1 + n2;
            System.out.print(n1 + " ");
        }
        System.out.println("\nFibonaci series using recursion::");
        for (int i = 0; i < num; i++) {
            System.out.print(fibonaci(i) + " ");
        }
    }
}
ouput: 
Fibonaci series using iteration::
0 1 1 2 3 
Fibonaci series using recursion::
0 1 1 2 3 
7. Palindrome

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.

For example Madam , Mom etc.

package com.commonlyasked;

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
output:
palindrome or not::true
8. Prime no generation between 2 numbers.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In other words, a prime number is a number that is divisible only by 1 and itself, and has no other factors.

For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, and so on, are prime numbers because they cannot be divided evenly by any other numbers except 1 and themselves.

package com.commonlyasked;

public class PrimeNo {
    public static void main(String[] args) {
        int first = 10;
        int second = 20;
        for (int i = first; i < second; i++) {
            boolean value = isPrime(i);
            if (value) System.out.println("Prime no::" + i);

        }

    }

    private static boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i < num; i++) {
            if (num % i == 0) return false;
        }

        return true;
    }
}
output :
Prime no::11
Prime no::13
Prime no::17
Prime no::19
9. Reverse a number

package com.commonlyasked;

public class ReverseANumber {
    public static void main(String[] args) {
        int num=123;
        int reverse = 0;
        System.out.println("Before Reversal of a number::"+ num);
        while (num !=0) {
            int remainder = num % 10;
            reverse = reverse * 10 + remainder;
            num = num / 10;
        }
        System.out.println("After Reversal of a number::"+ reverse);
    }
}
Output:
Before Reversal of a number::123
After Reversal of a number::321
10. Find Second Highest number in an unsorted array

package com.commonlyasked;

public class SecondHighest {
    public static void main(String[] args) {
        int[] arr = new int[]{4, 5, 2, 1, 9, 7};
        int highest = Integer.MIN_VALUE;
        int secondHighest = Integer.MIN_VALUE;
        for (int i = 0; i <= arr.length - 1; i++) {
            if (arr[i] > highest) {
                secondHighest = highest;
                highest = arr[i];
            } else if (arr[i] > secondHighest) {
                secondHighest = arr[i];
            }
        }
        System.out.println("Highest:: " + highest + "\nsecond highest::" + 
        secondHighest);
    }
}
output:
Highest:: 9
second highest::7
11. Reverse a string ( word or a sentence) iterative/recursive way.

package com.commonlyasked;

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
output :
olleH
expiry is today Hello 

Using recursion
olleH
12 . Find all pairs equal to a given sum

package com.commonlyasked;

import java.util.HashMap;
import java.util.Map;

public class FindPairsOfGivenSum {
    public static void main(String[] args) {
        int[] nums = new int[]{15, 12, 4, 16, 9, 8, 24, 0};
        int sum = 24;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length - 1; i++) {
            if (map.containsKey(sum - nums[i])) {
                System.out.println("pair found::" + (sum - nums[i]) + " " + nums[i]);
            }
            map.put(nums[i], i);
        }

    }
}
output:
pair found::15 9
pair found::16 8
13. Swap 2 numbers without using any inbuilt function

package com.commonlyasked;

public class SwapNumbers {

    public static void main(String[] a) {
        int x = 10;
        int y = 5;
        System.out.println("Before swapping:"
                + " x = " + x + ", y = " + y);
        x = x + y;
        y = x - y;
        x = x - y;
        System.out.println("After swapping:"
                + " x = " + x + ", y = " + y);
    }
}
output:
Before swapping: x = 10, y = 5
After swapping: x = 5, y = 10



// Set 1
// Fibonacci Series (with & without recursion)
// Prime numbers or Not
// Palindrome Number & Palindrome String
// Factorial Number (Using Recursion)
// Armstrong Number
// Set 2
// 6. Odd or Even Number

// 7. Sum of the digits & Sum of the natural numbers + count number of digits

// 8. Swapping of two numbers (with & without using third variable)

// 9. Number is strong or not

// 10. Perfect Number or Not

// 11. Harshad Number Program

// Set 3
// 12. Matrix Multiplication & Multiplication Table

// 13. Reversing of Number & Reverse a String (with & without using inbuilt functions)

// 14. Program to Convert Decimal to Binary & Binary to Decimal + Hexadecimal/ Octal to binary

// 15. Program for Leap Year or Not

// 16. Simple Calculator

// 17. Area of Circle, Rectangle & Triangle

// Set 4
// 18. Temperature Convertor [Fahrenheit to Celsius] + Vice-Verse

// 19. Grade Calculator

// 20. Vowels or Consonants Checker (count vowels and consonants / vowel is present in a string or not)

// 21. Fizz buzz Program

// 22. Anagram Checker / Check two strings are Anagram or not

// Set 5
// 23. GCD of two numbers & LCM

// Get Yuvraj Kevit’s stories in your inbox
// Join Medium for free to get updates from this writer.

// Enter your email
// Subscribe
// 24. Count Occurrence of a Character in a String

// 25. Check Two Strings are Relation of Each Other

// 26. Binary Search Program

// 27. Bubble Sort Program

// Set 6
// 28. Convert an array into a Zig-zag Pattern

// 29. Remove & Find Duplicates from an Array

// 30. Second Largest & Smallest Element in an Array

// 31. Find the Missing Number in an Array

// 32. Merge Sorted Array

// Set 7
// 33. Sum of an Array using Recursion

// 34. Maximum Subarray Sum (Kadane’s Algorithm)

// 35. Program for Duplicate Characters in a String

// 36. Program to Remove all white spaces from given string(with & without using built in functions)

// 37. How to solve Diamond Problem in Inheritance Program

// 38. Pattern Printing (Popular any 5)

// 39. How to generate random number in Java

// Set 8
// 40. Spy Number in Java

// 41. Automorphic Number in Java

// 42. Peterson Number in Java

// 43. Program to find smallest & largest of three numbers (Using Ternary Operator)

// 44. Type Conversion Program

// Set 9
// 45. Rotate a matrix by 90 degree in clockwise

// 46. Program for reverse a linked list

// 47. Permutation

// 48. Combination

// 49. check whether the string is alpha numeric or not.