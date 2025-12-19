package java_question1;

public class A4LeapYear3 {

	public static void main(String[] args) {
		
		int year = 700;
		/*
		 * if((year%4 == 0 && year%100 !=0) || (year%400 == 0)){
			System.out.println("this is a leap year");
		}
		else {
			System.out.println("This is not a leap year");
		}
		 */
		if (isLeapYear(year)) {
			System.out.println("this is a leap year");
		}
		else {
			System.out.println("this is not a leap year");
		}
		
	}
	
	public static boolean isLeapYear(int year) {
		return (year%4 == 0 && year%100 !=0) || (year%400 == 0);
	}

}
