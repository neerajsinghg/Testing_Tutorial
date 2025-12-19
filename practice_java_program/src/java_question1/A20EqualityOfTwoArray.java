package java_question1;

import java.util.Arrays;

public class A20EqualityOfTwoArray {

	public static void main(String[] args) {
		
		int[] a= {1,2,3,4,5};
		int[] b = {1,2,3,4,5,6};
		
		if(Arrays.equals(a, b)) {
			System.out.println("Arrays are equal");
		}
		else {
			System.out.println("Arrays are not equal");
		}

	}

}
