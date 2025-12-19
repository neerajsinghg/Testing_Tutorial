package src.smartpractice1;


public class SecondLargestSmallestNowithoutShort {

	public static void main(String[] args) {
		int [] no = {8,7,6,9,9,9};
		
		if(no.length<2) {
			System.out.println("element not enough ");
			return;
		}
		
		int largest = Integer.MIN_VALUE;
		int smallest = Integer.MAX_VALUE;
		
		for(int i=0; i<no.length; i++) {
			if(no[i]>largest) {
				largest = no[i];
			}
			if(no[i]<smallest) {
				smallest = no[i];
			}

		}
		System.out.println("largest = "+largest + " smallest = "+smallest);
		
		int sLargest = Integer.MIN_VALUE;
		int sSmallest = Integer.MAX_VALUE;
		
		for(int i=0; i<no.length; i++) {
			if(no[i]>sLargest && no[i]<largest) {
				sLargest = no[i];
			}
			if(no[i]<sSmallest && no[i]>smallest) {
				 sSmallest = no[i];
			}
		}
		System.out.println("second largest = "+sLargest);
		System.out.println("second smallest = "+ sSmallest);
		
	}

}
