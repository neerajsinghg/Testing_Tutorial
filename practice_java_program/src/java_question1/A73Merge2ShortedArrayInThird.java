package java_question1;

import java.util.Arrays;

public class A73Merge2ShortedArrayInThird {

	public static void main(String[] args) {
		
		int[] no1 = {12,3,4,5,6};
		int[] no2 = {34,7,8,9};
		int length = no1.length+no2.length;
		
		int[] result = new int[length];
		
		for(int i=0; i<no1.length; i++) {
			
				result[i]=no1[i];
		}
		for(int i=0; i<no2.length; i++) {
			result[i+no1.length]=no2[i];
		}
		Arrays.sort(result);
		System.out.println(Arrays.toString(result));

	}

}
