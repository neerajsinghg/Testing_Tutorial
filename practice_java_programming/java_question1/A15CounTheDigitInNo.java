package java_question1;

public class A15CounTheDigitInNo {

	public static void main(String[] args) {
		
		int no = 123456;
		/*
		 * String str = String.valueOf(no);
		System.out.println(str.length());
		 */
		int count = 0;
		while(no !=0) {
			no = no/10;
			count++;
		}
		System.out.println(count);

	}

}
