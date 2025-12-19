package basic_java;

//3. Count the no of 1’s without using any inbuilt function.

public class CountOfOnesWithoutInBuilt {
  public static void main(String[] args) {
      int[] arr = new int[]{1, 1, 0, 1, 0, 1, 1, 0};
      int sum = 0;
      for (int i : arr) {
          sum += i;
      }
      System.out.println("count of 1's::" + sum);
      System.out.println("count of 0's::" + (arr.length - sum));

  }
}
//output: 
//count of 1's::5
//count of 0's::3
