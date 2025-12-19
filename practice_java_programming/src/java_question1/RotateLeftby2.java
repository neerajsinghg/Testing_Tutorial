package java_question1;

public class RotateLeftby2 {

	public static void main(String[] args) {
		int [] no = {1,2,3,4,5,6,7};
		int first =no[0];
		int second = no[1];
		for(int i=0; i<no.length-2; i++) {
			no[i]=no[i+2];
			
		}
		no[no.length-2]=first;
		no[no.length-1]=second;
		
		for(int num:no) {
		System.out.print(num+" ");
		}
	}

}
