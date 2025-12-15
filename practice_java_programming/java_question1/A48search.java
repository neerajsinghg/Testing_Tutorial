package java_question1;

public class A48search {

	public static void main(String[] args) {
		
		int [] arr = {1,2,3,4,5,6,7,8,9};
		int targate = 15;
		boolean found = false;
		for(int num : arr) {
			if ( num==targate) {
			found=true;
			}
		}
		if(found == true) {
			System.out.println("targate is found");
		}
		else {
			System.out.println("element is not present");
		}
		

	}

}
