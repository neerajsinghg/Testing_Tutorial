package java_question1;

public class A30ReverseEachWord {

	public static void main(String[] args) {
		String str = "This is my pen";
		String[] str1 = str.split(" ");
		StringBuilder sb = new StringBuilder();
		for(String str2:str1) {
			char[] ch = str2.toCharArray();
			for(int i=ch.length-1; i>=0; i--) {
				sb.append(ch[i]);
			}
				sb.append(" ");
		}
		System.out.println(sb.toString().trim());
		
	}

}
