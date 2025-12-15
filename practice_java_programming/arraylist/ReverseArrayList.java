package arraylist;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class ReverseArrayList {

	public static void main(String[] args) {
		List<Integer> ls = new ArrayList<>();
		ls.add(1);
		ls.add(2);
		ls.add(3);
		ls.add(4);
		ls.add(5);
		ls.add(6);
		System.out.println(ls);
		ls.add(4, 10);
		System.out.println(ls);
		for(int num : ls) {
			System.out.print(num+" ");
		}
		System.out.println();
		Iterator<Integer> it = ls.iterator();
		while(it.hasNext()){ 
			System.out.print(it.next()+" ");
		}System.out.println();
		
		ListIterator<Integer> lt = ls.listIterator();
		while(lt.hasNext()) {
			System.out.print(lt.next()+", ");
		}
		System.out.println();
		ListIterator<Integer> lt1 = ls.listIterator(ls.size());
		while(lt1.hasPrevious()) {
			System.out.print(lt1.previous()+", ");
		}
		Collections.reverse(ls);
		System.out.println(ls);

	}

}
