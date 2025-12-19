package src.smartpractice1;

import java.util.Arrays;

public class SecondLargestAndSmallest {

	public static void main(String[] args) {
		int[] no = {45,66,77,98};
		Arrays.sort(no);
		System.out.println(Arrays.toString(no));
		if(no.length<2) {
			System.out.println("this is not enough array");
			return;
		}
		for(int i=0; i<no.length; i++) {
			if(no[0] !=no[i]) {
				System.out.println("second smallest = "+no[i]);
				break;
			}
		}
		for(int i=no.length-2; i>=0; i--) {
			if(no[no.length-1] !=no[i]) {
				System.out.println("second largest = "+no[i]);
				break;
			}
		}

	}

}
