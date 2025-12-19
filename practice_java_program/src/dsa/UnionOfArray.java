package dsa;

public class UnionOfArray {

    public static void unionOfTwoArray(int[] arr1, int[] arr2) {
        int i = 0, j = 0;

        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                System.out.print(arr1[i] + " ");
                i++;
            } else if (arr1[i] > arr2[j]) {
                System.out.print(arr2[j] + " ");
                j++;
            } else {
                // Same element, print once
                System.out.print(arr1[i] + " ");
                i++;
                j++;
            }
        }

        // Print remaining elements of arr1
        while (i < arr1.length) {
            System.out.print(arr1[i] + " ");
            i++;
        }

        // Print remaining elements of arr2
        while (j < arr2.length) {
            System.out.print(arr2[j] + " ");
            j++;
        }
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, 3, 4, 6, 9};
        int[] arr2 = {2, 3, 4, 5, 6, 7, 8, 9};

        unionOfTwoArray(arr1, arr2);
    }
}
