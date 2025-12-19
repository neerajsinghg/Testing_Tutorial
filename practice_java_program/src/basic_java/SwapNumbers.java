package basic_java;
//13. Swap 2 numbers without using any inbuilt function

public class SwapNumbers {

    public static void main(String[] a) {
        int x = 10;
        int y = 5;
        System.out.println("Before swapping:"
                + " x = " + x + ", y = " + y);
        x = x + y;
        y = x - y;
        x = x - y;
        System.out.println("After swapping:"
                + " x = " + x + ", y = " + y);
    }
}
//output:
//Before swapping: x = 10, y = 5
//After swapping: x = 5, y = 10