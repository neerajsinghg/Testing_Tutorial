package java_question1;

import java.util.Arrays;

public class A23BinarySearchElementInArray {

	public static void main(String[] args) {
		int[] a = {1,2,3,4,9,5,6,7,8};
		//Arrays.sort(a);
		int index = Arrays.binarySearch(a, 9);
		System.out.println(index);
	}

}
