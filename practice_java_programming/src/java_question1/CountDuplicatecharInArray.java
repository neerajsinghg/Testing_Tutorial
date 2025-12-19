package java_question1;

import java.util.HashMap;
import java.util.Map;

public class CountDuplicatecharInArray {

	public static void main(String[] args) {
		int [] no = {1,2,3,4,5,6,7,1,2,3};
		
		HashMap<Integer, Integer> hs = new HashMap<>();
		for(int num:no) {
			hs.put(num, hs.getOrDefault(num, 0)+1);
		}
		for(Map.Entry<Integer, Integer> entry : hs.entrySet()) {
			System.out.print(entry +" ");
		}

	}

}
