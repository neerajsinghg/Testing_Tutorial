package array_java;
//20. Dutch National Flag Problem (Sort an Array of 0s, 1s, and 2s):
//Given an array A [] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given array.
//Algorithm:
//Initialize three pointers: low, mid, and high.
//Traverse the array:
//If the current element is 0, swap it with the element at the low pointer and increment both low and mid.
//If the current element is 1, just increment mid.
//If the current element is 2, swap it with the element at the high pointer and decrement high.
//3. Continue until mid crosses high.

public class DutchNationalFlag {
    public static void main(String[] args) {
        int[] arr = {2, 0, 1, 2, 1, 0, 1, 0, 2};
sortColors(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
    private static void sortColors(int[] arr) {
        int low = 0;
        int mid = 0;
        int high = arr.length - 1;
        while (mid <= high) {
            switch (arr[mid]) {
                case 0:
                    swap(arr, low, mid);
                    low++;
                    mid++;
                    break;
                case 1:
                    mid++;
                    break;
                case 2:
                    swap(arr, mid, high);
                    high--;
                    break;
            }
        }
    }
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

//Q1. What’s the difference between Arrays.asList() and List.of()?
