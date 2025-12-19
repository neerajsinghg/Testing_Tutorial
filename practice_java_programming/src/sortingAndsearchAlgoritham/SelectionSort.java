package src.sortingAndsearchAlgoritham;

public class SelectionSort {
//Selection Sort mein hum minimum element dhundhte hain aur correct position pe swap karte hain. 
	//Har pass mein ek element apni sahi jagah par aa jaata hai
	public static void main(String[] args) {
		int[] arr = {1,2,3,6,5,4,7,9,21,31,23,53,35};
		int n = arr.length;
		
		for(int i=0; i<n-1; i++) {
			int miniIndex = i;
			for(int j=i+1; j<n; j++) {
				
				if(arr[j]<arr[miniIndex]) {
					miniIndex = j;
				}
				
			}
			int temp = arr[miniIndex];
            arr[miniIndex] = arr[i];
            arr[i] = temp;
		}
		System.out.println("sorted array = ");
		for(int num:arr) {
			System.out.print(num+" ");
		}
	}

}
