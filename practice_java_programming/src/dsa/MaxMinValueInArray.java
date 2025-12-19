package dsa;

public class MaxMinValueInArray {
	public static void maxMinValue(int[] no) {
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		
		for(int i =0; i<no.length;i++) {
			if(max<no[i]) {
				max=no[i];
			}
		}
		for(int i =0; i<no.length;i++) {
			if(min>no[i]) {
				min=no[i];
			}
	}
		System.out.println("Max value of array = "+max);
		System.out.println("Min value of array = "+min);
		}
	public static void main(String[] args) {
		int[] no= new int[] {1,5,4,21,7,3,9};
		maxMinValue(no);

	}

}
