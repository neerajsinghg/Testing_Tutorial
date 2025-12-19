package java_question1;
import java.util.*;
public class RevWordUsingCollection {

	public static void main(String[] args) {
		String str = "this is my pen";
		String[] word = str.split(" ");
		List<String> al = new ArrayList<>();
		for(int i=word.length-1; i>=0;i--) {
			al.add(word[i]);
		}
		System.out.println(al);
		Object obj = al.toString();
		System.out.println(obj.getClass().getSimpleName());
	}

}
