package sortingAndsearchAlgoritham;

public class Bubblesort {
/*
 * Bubble Sort mein adjacent elements ko compare karte hain, swap karte hain agar needed ho, 
 * aur bada element har pass mein end mein pahunchta hai — jaise bubble surface pe aata hai
 */
	public static void main(String[] args) {
		int [] arr = { 4,5,3,1,2,7,9,8};
		int n = arr.length;

		for(int i=0; i<n; i++) {
			for(int j=0; j<n-i-1; j++) {
				if(arr[j]>arr[j+1]) {
					int temp = arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;
				}
			}		
		}
		System.out.println("sorted array = ");
		for(int num :arr) {
			System.out.print(num+" ");
		}
	}

}
