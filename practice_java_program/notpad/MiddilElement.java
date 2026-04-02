public class MiddilElement{
	public static void main(String[] args){
		int[] numbers = {2,3,4,5,6,7,3,1};
		int left=0;
		int right=numbers.length-1;
		while(left<=right){
			left++;
			right--;
		}
		if(left==right){
			System.out.println(numbers[left]);
		}
		else{
			System.out.println("There are two middle element one is "+ numbers[left-1]+" another is "+ numbers[left]);
		}
	}
}


public class MiddilElement {
    public static void main(String[] args) {

        int[] numbers = {2,3,4,5,6,7,3,1};

        int n = numbers.length;

        if(n % 2 == 1){
            // Odd length → one middle
            System.out.println("Middle element = " + numbers[n/2]);
        } else {
            // Even length → two middle
            System.out.println("Two middle elements are: "
                + numbers[(n/2) - 1] + " and " + numbers[n/2]);
        }
    }
}