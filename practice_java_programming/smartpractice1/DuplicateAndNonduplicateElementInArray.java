package smartpractice1;

import java.util.ArrayList;
import java.util.HashMap;

import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class DuplicateAndNonduplicateElementInArray {

	public static void main(String[] args) {
		
		int [] no  = {1,2,4,5,6,1,2,3,4,8,9,9,9};
		Map<Integer,Integer> hs = new HashMap<>();
		List<Integer> l = new LinkedList<>(); 
		List<Integer> ll = new ArrayList<>();
		for(int num :no) {
			hs.put(num, hs.getOrDefault(num, 0)+1);		
		}
		System.out.println(hs);
		for(Map.Entry<Integer, Integer> entry : hs.entrySet()) {
			if(entry.getValue()>1) {
				l.add(entry.getKey());
			}
			else {
				ll.add(entry.getKey());
			}
		}
		System.out.println(l);
		System.out.println(ll);
	}

}
