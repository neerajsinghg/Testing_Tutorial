package basic_java;

//10. Find Second Highest number in an unsorted array

public class SecondHighest {
    public static void main(String[] args) {
        int[] arr = new int[]{4, 5, 2, 1, 9, 7};
        int highest = Integer.MIN_VALUE;
        int secondHighest = Integer.MIN_VALUE;
        for (int i = 0; i <= arr.length - 1; i++) {
            if (arr[i] > highest) {
                secondHighest = highest;
                highest = arr[i];
            } else if (arr[i] > secondHighest) {
                secondHighest = arr[i];
            }
        }
        System.out.println("Highest:: " + highest + "\nsecond highest::" + 
        secondHighest);
    }
}
//output:
//Highest:: 9
//second highest::7