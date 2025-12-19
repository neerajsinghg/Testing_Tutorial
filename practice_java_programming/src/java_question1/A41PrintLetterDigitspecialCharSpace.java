package java_question1;

public class A41PrintLetterDigitspecialCharSpace {

	public static void main(String[] args) {
		String str = "This is 234 my #$% pen";
		int count =0;
		char [] ch = str.toCharArray();
		StringBuilder sb = new StringBuilder();
		StringBuilder sb1 = new StringBuilder();
		StringBuilder sb2 = new StringBuilder();
		for(char ch1 : ch) {
			if(Character.isAlphabetic(ch1)) {
				sb.append(ch1);
			}
			else if(Character.isDigit(ch1)) {
				sb1.append(ch1);
			}
			else if(ch1 ==' ') {
				count+=1;
			}
			else {
				sb2.append(ch1);
			}
		}
		System.out.println("alphabates = "+sb.toString());
		System.out.println("digit = "+sb1.toString());
		System.out.println("special char = "+sb2.toString());
		System.out.println("no of spaces are = "+count);
	}

}
