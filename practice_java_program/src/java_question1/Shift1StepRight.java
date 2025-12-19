package java_question1;



public class Shift1StepRight {

	public static void main(String[] args) {
		
		//Integer[] no = {1,2,3,4,5,6,7,8,9};
		
		/*
		 int first = no[0];
		
		for(int i=0; i<no.length-1; i++) {
			no[i]=no[i+1];
		}
		no[no.length-1]=first;
		for(int num : no) {
			System.out.print(num + " ");
		}
		 */
		/*
		 ArrayList<Integer> list = new ArrayList<>();
		for(int num:no) {
		list.add(num);
	}
		int rot= list.remove(0);
		list.add(rot);
		System.out.println(list);
		 */
		/*
		 *  ArrayList<Integer> list = new ArrayList<>();
		 Collections.addAll(list, no);
		 Collections.rotate(list, 2);
		 System.out.println(list);
		 */
		
		int[] num = {1,2,3,4,5,6,7,8,9};
		
		int last = num[num.length-1];
		int secondlast = num[num.length-2];
		
		for(int i=num.length-3; i>1; i--) {
		num[i]=num[i-2];
		
	}
		num[0] = secondlast;
		num[1] = last;
		
		for(int num1:num) {
			System.out.print(num1+" ");
		}
	
	}

}
