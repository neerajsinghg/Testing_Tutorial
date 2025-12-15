package java_question1;

import java.util.Arrays;

public class RotateArray {

	public static void main(String[] args) {
		int [] no = {1,2,3,4,5,6,7};
		int last =no[no.length-1];
		
		for(int i=no.length-1; i>0; i--) {
			no[i]= no[i-1];
		}
			no[0]=last;
		System.out.println(Arrays.toString(no));
		for(int num :no) {
			System.out.print(num+" ");
		}
		
		

	}

}
