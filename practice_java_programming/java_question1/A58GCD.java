package java_question1;

public class A58GCD {

	public static void main(String[] args) {
		
		int first=12;
		int second=18;
		int gcd = 0;
		
		for(int i=1; i<=first; i++) {
			if (first%i == 0 && second%i==0) {
				//System.out.print(i+" ");
				gcd=i;
			}
			
		}
		System.out.println("gcd = "+gcd);
		

	}

} 
