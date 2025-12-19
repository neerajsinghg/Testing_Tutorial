package src.smartpractice;

import java.util.Arrays;

public class RightRotateByK {

	public static void main(String[] args) {
		
		int [] no = {17,4,2,9,6,3};//	{9,6,3,17,4,2}
		
		/*
		 List<Integer> list = new ArrayList<>();
		for(int num :no) {
			list.add(num);
		}
		
		Collections.rotate(list, 3);
		System.out.println(list);
		 */
		int shift =4;
		int n = no.length;
		int[] result = new int[n];
		
		for(int i=0; i<=n-1;i++) {
			result[(i+shift)%n] = no[i];
		}
		System.out.println(Arrays.toString(result));
		
		
	}

}
