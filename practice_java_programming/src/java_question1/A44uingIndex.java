package java_question1;

import java.util.ArrayList;
import java.util.Arrays;

public class A44uingIndex {

	public static void main(String[] args) {
		
		int[] no = {1,2,3,4,5,6,7,1,2,3,4};
		Arrays.sort(no);
		ArrayList<Integer> al = new ArrayList<>();
		ArrayList<Integer> al1 = new ArrayList<>();
		
		for(int i=0; i<no.length-1; i++) {
			if(no[i]==no[i+1]) {
				al.add(no[i]);
			}
			else {
				al1.add(no[i]);
			}
		}
		System.out.println("duplicate element " + al);
		System.out.println(al1);

	}

}
