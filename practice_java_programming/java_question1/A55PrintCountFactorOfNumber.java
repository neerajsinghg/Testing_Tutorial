package java_question1;

public class A55PrintCountFactorOfNumber {

	public static void main(String[] args) {
		
		int no=60;
		int count = 0;
		System.out.println("Factors of a number = ");
		for(int i=1; i<=60; i++) {
			if (no%i==0) {
				System.out.print(i+" ");
				count+=1;
			}
		}
		System.out.println();
		System.out.println("total no factors = " +count);

	}

}
