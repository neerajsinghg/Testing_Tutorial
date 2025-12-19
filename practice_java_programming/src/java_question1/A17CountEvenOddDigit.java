package java_question1;

public class A17CountEvenOddDigit {

	public static void main(String[] args) {
		
		int no = 123456789;
		int even = 0;
		int odd = 0;
		String str = Integer.toString(no);
		
		char [] chno = str.toCharArray();
		for(char ch : chno) {
			if(ch%2==0) {
				even+=1;
			}
			else {
				odd +=1;
			}
		}
		System.out.println(even);
		System.out.println(odd);

	}

}
