package java_question1;

public class A8ReverseNo {

	public static void main(String[] args) {
		
		/**
		 * int no=1234;
		int rev = 0;
		while (no !=0) {
			int digit = no%10; //get last digit
			rev = rev*10+digit;
			no=no/10;
		}
		System.out.println(rev);
		 */
		int no =89734;
		String no1 = String.valueOf(no);
		StringBuilder sb = new StringBuilder();
		String no2 = sb.append(no1).reverse().toString();
		System.out.println(Integer.parseInt(no2));
	}

}
