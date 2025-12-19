package array_java;
//14. Find Second Largest Element in an Array:
//Algorithm:

//Initialize variables max and secondMax to Integer.MIN_VALUE.
//Iterate through each element in the array.
//If the current element is greater than max, update secondMax to max and max to the current element.
//If the current element is greater than secondMax but less than max, update secondMax to the current element.
//Print the value of secondMax.

public class SecondLargestElement {
    public static void main(String[] args) {
        int[] numbers = {5, 8, 2, 1, 9, 3};
int secondLargest = findSecondLargest(numbers);
        System.out.println("Second Largest Element: " + secondLargest);
    }
    private static int findSecondLargest(int[] arr) {
        int max = Integer.MIN_VALUE;
        int secondMax = Integer.MIN_VALUE;
        for (int num : arr) {
            if (num > max) {
                secondMax = max;
                max = num;
            } else if (num > secondMax && num != max) {
                secondMax = num;
            }
        }
        return secondMax;
    }
}
