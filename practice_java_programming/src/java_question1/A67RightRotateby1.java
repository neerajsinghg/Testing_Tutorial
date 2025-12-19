package java_question1;

import java.util.Arrays;

public class A67RightRotateby1 {

	public static void main(String[] args) {
		int [] no = {1,2,3,4,5,6,7,8};//{8,1,2,3,4,5,6,7}
		int shift=3;
		int n=no.length;
		int[] result = new int[no.length];
		
		for(int i=0; i<n; i++) {
			result[(i+shift)%n] = no[i];
		}
		System.out.println(Arrays.toString(result));

	}

}
