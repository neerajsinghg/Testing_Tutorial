package java_question1;

public class A26RemoveSpecialCharFromString {

	public static void main(String[] args) {
		String str = "Thsis@#$gjeid";
		/*
		 char[] arr = str.toCharArray();
		StringBuilder sb = new StringBuilder();
		for(char ch : arr) {
			if (Character.isAlphabetic(ch)) {
				sb.append(ch).toString();
			}
		
		}
		System.out.println(sb);

		 */
		str = str.replaceAll("[^a-zA-Z]", "");
		 // str = str.replaceAll("[^a-zA-Z]", "");
		System.out.println(str);
		
	}

}
