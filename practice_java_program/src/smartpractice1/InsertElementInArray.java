package smartpractice1;

import java.util.Arrays;

public class InsertElementInArray {

	public static void main(String[] args) {
		int [] no = {10,20,30,40,50,60};
		int insertElement=25;
		int position=no.length/2;
		
		int[] num = new int[no.length+1];
		for(int i=0,j=0; i<num.length; i++) {
			
			if(i==position) {
				num[i] = insertElement;
			}
			else {
				num[i]=no[j];
				j++;
			}
		}
		System.out.println(Arrays.toString(num));

	}

}
