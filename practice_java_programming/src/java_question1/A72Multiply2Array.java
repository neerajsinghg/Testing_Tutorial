package java_question1;

import java.util.Arrays;

public class A72Multiply2Array {

	public static void main(String[] args) {
		
		int [] no1 = {2,3,4,5};
		int [] no2 = {6,7,8,9};
		
		int [] result = new int[no1.length];
		
		for(int i=0; i<=no1.length-1; i++) {
			result[i]=no1[i]*no2[i];
		}
		System.out.println(Arrays.toString(result));
	}

}
