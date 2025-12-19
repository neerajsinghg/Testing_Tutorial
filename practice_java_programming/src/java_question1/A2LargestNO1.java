package java_question1;

public class A2LargestNO1 {

	public static void main(String[] args) {
		int i = 50;
		int j = 70;
		int k = 40;
		if(i>j && i>k) {
			System.out.println(i+ " is greater than "+j +" and " +k);
			
		}
		else if (j>i && j>k) {
			System.out.println(j+" is greater than "+i +" and " +k  );
		}
		else {
			System.out.println(k+ " is greater than "+i+" and "+j);
		}

	}

}
