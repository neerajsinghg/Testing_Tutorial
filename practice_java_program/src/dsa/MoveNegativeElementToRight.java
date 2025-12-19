package dsa;

import java.util.Arrays;

public class MoveNegativeElementToRight {
	public static void NegativeEleToRight(int [] no) {
		int[] result = new int[no.length];
		int k=0;
		for(int i=0; i<no.length; i++) {
			if(no[i]>0) {
				result[k]=no[i];
				k++;
			}

		}
		for(int i=0; i<no.length; i++) {
			if(no[i]<0) {
				result[k]=no[i];
				k++;
			}
		}
		System.out.println(Arrays.toString(result));
	}
	public static void main(String[] args) {
		int [] no = {5,4,3,-1,-4,-9,-5,2,5,-8,9};
		NegativeEleToRight(no);
	}
}
