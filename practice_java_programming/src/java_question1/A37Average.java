package java_question1;

public class A37Average {

	public static void main(String[] args) {
		
		/*
		 int a = 10, b=20, c=30, d=40, e=50;
		float c1 = (float) (a+b+c+d+e)/5;
		int c2 = (int) c1;
		System.out.println(c2);
		 */
		
		int[] no= {1,2,3,4,5,6,7,8};
		int sum = 0;
		int n= no.length;
		System.out.println(n);
		for(int no1 :no) {
			sum +=no1;
		}
		System.out.println(sum);
		float ave = (float)sum/n;
		System.out.println(ave);

	}

}
