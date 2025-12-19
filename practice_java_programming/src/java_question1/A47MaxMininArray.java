package java_question1;

public class A47MaxMininArray {

	public static void main(String[] args) {
		int [] no = {1,2,3,4,5,6,7,8};
		int mini = no[0];
		int max = no[0];
		
		for(int num : no) {
			if(mini>num) {
				mini=num;
			}
			if(max<num) {
				max=num;
			}
		}
		System.out.println(mini);
		System.out.println(max);

	}

}
