package java_question1;

import java.util.HashSet;

public class A44DuplicateelementusingHashset {

	public static void main(String[] args) {
		
		Integer[] no = {1,2,3,4,5,6,1,2,3};
		HashSet<Integer> hs = new HashSet<>();
		HashSet<Integer> hs1 = new HashSet<>();
		for(int num : no) {
			if(!hs.add(num)) {
				hs1.add(num);
			}
			
		}
		System.out.println(hs);
		System.out.println(hs1);
		
		
		

	}

}
