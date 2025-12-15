package java_question1;

public class A9ReverseString {

	public static void main(String[] args) {
		String str = "this is my pen";
		String[] arr = str.split(" ");
		StringBuilder sb = new StringBuilder();
		for(String  arr1 : arr) {
			char[] ch = arr1.toCharArray();
			for(int i=ch.length-1; i>=0; i--) {
				sb.append(ch[i]);
				
			}
			sb.append(" ");
		}
		System.out.println(sb);

	}

}
