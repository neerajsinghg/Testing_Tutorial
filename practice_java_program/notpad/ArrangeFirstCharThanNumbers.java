import java.util.*;
public class ArrangeFirstCharThanNumbers{
	public static void main(String[] args){
		Object[] arr = {1,'a','b',2,'c',3,'d',4,5,'f'};
		List<Integer> l1 = new ArrayList<>();
		List<Character> l2 = new ArrayList<>();
		for(Object ar:arr){
			if(ar instanceof Integer){
				l1.add((Integer)ar);
			}
			else if(ar instanceof Character){
				l2.add((Character)ar);
			}
		}
		List<Object> list = new ArrayList<>();
			list.addAll(l2);
			list.addAll(l1);
		System.out.println(list);
	}
}