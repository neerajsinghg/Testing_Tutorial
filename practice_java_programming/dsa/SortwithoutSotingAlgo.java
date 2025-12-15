package dsa;

import java.util.Arrays;

public class SortwithoutSotingAlgo {
	
	public static void sortAlgo(int[] no) {
		int count0=0;
		int count1=0;
		int count2=0;

		for(int num :no) {
			if(num == 0) {
				count0++;
			}
			if(num == 1) {
				count1++;
			}
			if(num == 2) {
				count2++;
			}
		}
		System.out.println("0 = "+count0+", 1 = "+count1+", 2 = "+count2);
		int idx=0;
		for(int i=0; i<count0; i++) {no[idx++]=0;}
		for(int i=0; i<count1; i++) {no[idx++]=1;}
		for(int i=0; i<count2; i++) {no[idx++]=2;}
		System.out.println(Arrays.toString(no));
		System.out.println();
		int [] no1 = {0,1,2,0,1,2,0,1,2};
		Arrays.sort(no1);
		System.out.println(Arrays.toString(no1));
		
	}

	public static void main(String[] args) {
		int [] no = {0,1,2,0,1,2,0,1,2};
		
		sortAlgo(no);

	}

}
