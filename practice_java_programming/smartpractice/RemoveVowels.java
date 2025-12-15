package smartpractice;

public class RemoveVowels {

	public static void main(String[] args) {
		/*
		 String str = "No lemon";
		str= str.replaceAll("[aeiou]", "");
		System.out.println(str);
		 */
		String str = "No lemon";
		char [] ch=str.toCharArray();
		StringBuilder sb = new StringBuilder();
		for(char ch1: ch) {
			if(!(ch1 =='a'||ch1=='e'||ch1=='i'||ch1=='o'||ch1=='u')) {
				sb.append(ch1);
			}
		}
		System.out.println(sb.toString());

	}

}
