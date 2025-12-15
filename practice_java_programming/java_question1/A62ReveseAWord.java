package java_question1;

import java.util.ArrayList;
import java.util.Collections;

public class A62ReveseAWord {

	public static void main(String[] args) {
		String sentence = "This is my pen";
		String[] word = sentence.split(" ");
		ArrayList<String> al = new ArrayList<>();
		StringBuilder sb = new StringBuilder();
		for(String str : word) {
			al.add(str);
			sb.append(str).append(" ");
		}
		Collections.reverse(al);
		sb.reverse();
		System.out.println(al );
		System.out.println(sb.toString().trim() );
		
		
			
				
				

	}

}
