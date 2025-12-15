package java_question1;

import java.util.Random;

public class A46RandomNo {

	public static void main(String[] args) {
		Random rand = new Random();
		int no = rand.nextInt(100, 300);
		System.out.println(no);

	}

}
