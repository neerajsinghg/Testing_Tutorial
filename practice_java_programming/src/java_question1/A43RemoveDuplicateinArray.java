package java_question1;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;

public class A43RemoveDuplicateinArray {

	public static void main(String[] args) {
		
		String str = "java is good and java is most powerfull";
		String[] str1 = str.split(" ");
		HashSet<String> hs = new HashSet<>(Arrays.asList(str1));
		ArrayList<String> list = new ArrayList<>(Arrays.asList(str1));
		Collections.reverse(list);
		System.out.println(list);
		System.out.println(hs);
		
		

	}

}
