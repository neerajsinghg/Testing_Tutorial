package java_question1;

public class A11PrimeNo1to100 {

	public static void main(String[] args) {
		int no=100;
		System.out.println("This is a prime no betwen 1 to 100");
		for(int i=2; i<=no; i++) {
		boolean isPrime=true;
		for(int j=2; j<i; j++) {
			if(i%j==0) {
			isPrime = false;
			break;
			}
			
		}
		
		if(isPrime) {
			System.out.print( i +" ");
		}

	}

	}}
