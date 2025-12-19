package dsa;

import java.util.ArrayList;

public class MoveNegativeElement {
	public static void negativeElementInRight(int[] no) {
		ArrayList<Integer> l = new ArrayList<>();
		ArrayList<Integer> ll = new ArrayList<>();
		
		for(int num :no) {
			if(num<0) {
				l.add(num);
			}
			else if(num>0){
				ll.add(num);
			}
		}
		ArrayList<Integer> lll = new ArrayList<>();
		lll.addAll(l);
		lll.addAll(ll);
		System.out.println(lll);
	}

	public static void main(String[] args) {
		int [] no = {-1,-2,4,5,6,7,-3,-8};
		negativeElementInRight(no);

	}

}
