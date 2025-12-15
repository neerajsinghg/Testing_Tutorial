package java_question1;

public class A27RemoveWhiteSpace {

	public static void main(String[] args) {
		
		String str = "This is my pen";
		String[] str1 = str.split(" ");
		//str = str.replaceAll(" ", "");
		//System.out.println(str);
		StringBuilder sb = new StringBuilder();
		for(String str2 : str1) {
			sb.append(str2);
		}
		System.out.println(sb.toString());
		
	}

}
