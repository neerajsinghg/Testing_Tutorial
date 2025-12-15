package java_question1;

public class A18CountSumOfDigit {

	public static void main(String[] args) {
		
		int no = 123456789;
		int sum = 0;
		
		/*
		  String str = Integer.toString(no);
		
		char [] chno = str.toCharArray();
		for(char ch : chno) {
			//sum +=ch-'0';
			sum += Character.getNumericValue(ch);
			
		}
		System.out.println(sum);
		 */
		while(no>0) {
			sum += no%10;
			no = no/10;
		}
		System.out.println(sum);
		
	}

}
