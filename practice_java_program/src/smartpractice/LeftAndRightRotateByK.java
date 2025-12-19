package smartpractice;

import java.util.Arrays;

public class LeftAndRightRotateByK {
    public static void main(String[] args) {

        int[] no = {17, 4, 2, 9, 6, 3, 1}; // Original array left={9,6,3,1,17,4,2}, Right={6,3,1,17,4,2,9}
        int shift = 3;
        int n = no.length;

        // Left Rotation
        int[] leftResult = new int[n];
        for (int i = 0; i < n; i++) {
            leftResult[i] = no[(i + shift) % n];
        }
        System.out.println("Left rotate of array = " + Arrays.toString(leftResult));

        // Right Rotation
        int[] rightResult = new int[n];
        for (int i = 0; i < n; i++) {
            rightResult[(i + shift) % n] = no[i];
        }
        System.out.println("Right rotate of array = " + Arrays.toString(rightResult));
    }
}
