package java_question1;

import java.util.ArrayList;
import java.util.Collections;

public class A60ReverseArray {

	public static void main(String[] args) {
		Integer[] no = {1,2,3,4,5,6,7,8,9,10};
		ArrayList<Integer> ls = new ArrayList<>();
		for(int num : no) {
			ls.add(num);
		}
		Collections.reverse(ls);
		System.out.println(ls);
	}

}
