package java_question1;

import java.util.Arrays;

public class MergeTwoArray {

	public static void main(String[] args) {
		int [] arr1 = {1,2,3,4,5};
		int [] arr2 = {6,7,8,9,10};
		
		int length1 = arr1.length;
		int length2 = arr2.length;
		
		int[] arr3 = new int[length1+length2];
		for(int i=0; i<length1; i++) {
			arr3[i] = arr1[i];
		}
		for(int i=0; i<length2; i++) {
			arr3[length1+i] = arr2[i];
		}
		System.out.println(Arrays.toString(arr3));

	}

}
