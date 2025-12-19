package java_question1;

public class A10PrimeNo {

	public static void main(String[] args) {
		
		int no =17;
		boolean isPrime=true;
		for(int i=2; i<no; i++) {
			if(no%i==0) {
			isPrime = false;
			}
			
		}
		if(isPrime) {
			System.out.println("this is a prime no");
		}
		else {
			System.out.println("this is not a prime no");
		}

	}

}
