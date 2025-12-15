package java_question1;

import java.util.Arrays;

public class A21MissingNoInArrays {

	public static void main(String[] args) {
		
		int [] no = {1,2,3,4,5,7,6,9};
		
		/*
		 int n=no.length+1;
		int expectedSum = n*(n+1)/2;
		int actualSum = 0;
		
		for(int no1:no) {
			actualSum +=no1;
		}
		int missingNo= expectedSum-actualSum;
		System.out.println(missingNo);
		 */
		Arrays.sort(no);
		for(int i=0; i<no.length-1;i++) {
			if(no[i+1]!=no[i]+1) {
				System.out.println("missing number = "+ (no[i]+1));
				break;
			}
		}
		
	}

}
