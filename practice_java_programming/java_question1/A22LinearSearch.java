package java_question1;

public class A22LinearSearch {

	public static void main(String[] args) {
		
		int [] array = {11,10,1,2,3,4,5,6,7,8};
		int targate = 11;
		int index= -1;
		for( int i=0; i<=array.length-1; i++) {
			if(array[i]==targate) {
				index=i;
			}
		}
		if (index !=-1) {
			System.out.println(index);
		}else {
			System.out.println("targate is not found");
		}

	}

}
