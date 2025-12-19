package java_question1;

public class A30ReverseString {

	public static void main(String[] args) {
		String str = "This is my pen";
		String[] str1 = str.split(" ");
		StringBuilder sb = new StringBuilder();
		for (int i=str1.length-1; i>=0;i--) {
			sb.append(str1[i]).append(" ");
		}
		System.out.println(sb.toString().trim());
	}

}
