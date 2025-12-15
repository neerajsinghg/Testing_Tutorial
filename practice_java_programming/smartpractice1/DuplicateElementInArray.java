package smartpractice1;

import java.util.HashSet;
import java.util.Set;

public class DuplicateElementInArray {

	public static void main(String[] args) {
		int [] no  = {1,2,4,5,6,1,2,3,4,8,9,4};
		Set<Integer> hs = new HashSet<>();
		Set<Integer> duplicate = new HashSet<>();
		
		for(int num : no) {
			if(!hs.add(num)) {
				duplicate.add(num);
			}
		}
		System.out.println(duplicate);

	}

}
