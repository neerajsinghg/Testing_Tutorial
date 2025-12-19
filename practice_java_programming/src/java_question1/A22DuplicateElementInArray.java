package java_question1;
import java.util.HashSet;

public class A22DuplicateElementInArray {

	public static void main(String[] args) {

		int[] a = {1,2,3,4,5,5,6,6,2};

		/*
		 *Arrays.sort(a);
		for(int i=0; i<a.length-1; i++) {
			if(a[i] ==a[i+1]) {
				System.out.println("duplicate element is = "+a[i]);
			}
		}
		 */
		HashSet<Integer> seen=new HashSet<>();
		HashSet<Integer> duplicate=new HashSet<>();
		for(int a1:a) {
			if(!seen.add(a1)) {
				duplicate.add(a1);
			}
		}
		System.out.println("Duplicate no " +duplicate);
	}
}
