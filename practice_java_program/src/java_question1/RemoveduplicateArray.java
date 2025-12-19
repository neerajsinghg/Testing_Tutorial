package java_question1;

import java.util.HashSet;

public class RemoveduplicateArray {

	public static void main(String[] args) {
		
		int[] no= {1,2,3,4,5,6,6,7};
		HashSet<Integer> hs = new HashSet<>();
		
		for(int num:no) {
			
			hs.add(num);
		}
		System.out.println(hs);

	}

}
