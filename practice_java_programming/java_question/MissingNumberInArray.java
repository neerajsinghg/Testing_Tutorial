/**
 * find missing no in natural in given array;
 */
package java_question;

public class MissingNumberInArray {
    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 5, 6}; // Array with missing number
        int missingNumber = findMissingNumber(arr);
        System.out.println("Missing number is: " + missingNumber);
    }

    public static int findMissingNumber(int[] arr) {
        int n = arr.length + 1; // Since one number is missing
        int expectedSum = (n * (n + 1)) / 2;
        int actualSum = 0;

        for (int num : arr) {
            actualSum += num;
        }

        return expectedSum - actualSum;
    }
}
