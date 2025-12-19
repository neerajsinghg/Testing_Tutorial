/*
 * array either increasing order or decreasing array
 */
package java_question;

public class MonotonicArray {
    public static void main(String[] args) {
        int a[] = {1, 2, 3, 4}; // Example array

        boolean increasing = true;
        boolean decreasing = true;

        // Loop through the array and check for monotonicity
        for (int i = 1; i < a.length; i++) {
            if (a[i - 1] < a[i]) {
                decreasing = false; // Not decreasing
            } else if (a[i - 1] > a[i]) {
                increasing = false; // Not increasing
            }
        }

        // If the array is either increasing or decreasing, it is monotonic
        if (increasing || decreasing) {
            System.out.println("The given array is monotonic");
        } else {
            System.out.println("The given array is not monotonic");
        }
    }
}

