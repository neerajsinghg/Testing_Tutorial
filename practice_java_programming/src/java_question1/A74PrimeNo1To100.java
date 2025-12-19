package java_question1;

public class A74PrimeNo1To100 {

	public static void main(String[] args) {
		int no = 19;
		Boolean isPrime=true;
		
		for(int i= 2; i<no; i++) {
			if(no%i == 0) {
			isPrime=false;
			break;
			}
			
		}
		if(isPrime) {
			System.out.println("this is prim no");
		}
		else{
			System.out.println("this is not a prime no");
		}
	}

}
