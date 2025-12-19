package smartpractice;

import java.util.Arrays;

public class A71SwapFirstAndlast {

	public static void main(String[] args) {
		int[] no = {1,2,3,4,5,6};
		int last = no[no.length-1];
		int first = no[0];
		int temp=0;
		
		temp=no[0];
		no[0] = no[no.length-1];
		no[no.length-1] = temp;
		
		System.out.println("first " +first + " and last "+last);
		System.out.println(Arrays.toString(no));
		
	}
	

}
