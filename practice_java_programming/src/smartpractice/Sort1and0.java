package src.smartpractice;

//import java.util.Arrays;
//
//public class Sort1and0 {
//
//	public static void main(String[] args) {
//		int[] arr = {1, 0, 1, 0, 1, 0};
//		
//		for(int i=0, j=arr.length-1; i<j;) {
//			if( arr[i]==1 && arr[j]==0) {
//				int temp=arr[i];
//				arr[i]=arr[j];
//				arr[j]=temp;
//				i++;
//				j--;
//			}
//			else if(arr[i]==1 && arr[j]==1)  {
//				j--;
//			}
//			else if(arr[i]==0 && arr[j]==0) {
//				i++;
//			}
//			else {
//				j--;
//				i++;
//			}
//		}
//		System.out.println(Arrays.toString(arr));
//		
//	}
//
//}





import java.util.Arrays;

public class Sort1and0 {
    public static void main(String[] args) {
        int[] arr = {0, 1, 2, 3, 4, 1, 0, 0, 0, 1};

        // Step 1: Count 0s and 1s
        int countZero = 0, countOne = 0;
        for (int num : arr) {
            if (num == 0) countZero++;
            else if (num == 1) countOne++;
        }

        // Step 2: Fill array back with 0s and 1s
        int[] result = new int[countZero + countOne];
        int index = 0;

        // Put all 0s
        for (int i = 0; i < countZero; i++) {
            result[index++] = 0;
        }

        // Put all 1s
        for (int i = 0; i < countOne; i++) {
            result[index++] = 1;
        }

        System.out.println("Filtered & Sorted Array (DSA): " + Arrays.toString(result));
    }
}

