package array_java;
//15. Merge Two Sorted Arrays:
//Algorithm:
//Initialize an empty array to store the merged result.
//Initialize pointers i, j, and k to 0 to track the positions in the two input arrays and the merged array, respectively.
//Compare elements from both arrays and add the smaller one to the merged array.
//Increment the pointer of the array from which the element was added and the pointer for the merged array.
//Repeat until both input arrays are completely traversed.
//Copy any remaining elements from either array to the merged array.
//Return the merged array.

public class MergeSortedArrays {
    public static void main(String[] args) {
        int[] arr1 = {1, 3, 5, 7};
        int[] arr2 = {2, 4, 6, 8};
int[] mergedArray = mergeArrays(arr1, arr2);
        System.out.println("Merged Array:");
        for (int num : mergedArray) {
            System.out.print(num + " ");
        }
    }
    private static int[] mergeArrays(int[] arr1, int[] arr2) {
        int[] mergedArray = new int[arr1.length + arr2.length];
        int i = 0, j = 0, k = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                mergedArray[k++] = arr1[i++];
            } else {
                mergedArray[k++] = arr2[j++];
            }
        }
        while (i < arr1.length) {
            mergedArray[k++] = arr1[i++];
        }
        while (j < arr2.length) {
            mergedArray[k++] = arr2[j++];
        }
        return mergedArray;
    }
}