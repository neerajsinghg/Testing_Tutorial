package java_question;
/**
 * count a char in given string without using length().
 */

public class Count_Char {

	public static void main(String[] args) {
		
		String str = "Hello java";
		int count =0;
		char [] ch = str.toCharArray();
		StringBuffer sb = new StringBuffer();
		for(char ch1 : ch) {
			if(ch1 == ' ') {
				continue;
			}
			else {
				count++;
			}
			sb.append(ch1);
			
		}
		System.out.println(count);
		System.out.println(sb.toString().trim());

	}

}
