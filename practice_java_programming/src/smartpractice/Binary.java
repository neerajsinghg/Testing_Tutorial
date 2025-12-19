package src.smartpractice;

import java.util.Arrays;

public class Binary {

	public static void main(String[] args) {
		
		String binaryno = "0101010101";   //output   [0, 0, 0, 0, 1, 1, 1, 1]
		char [] ch = binaryno.toCharArray();
		Arrays.sort(ch);
		System.out.println(Arrays.toString(ch));

	}

}
