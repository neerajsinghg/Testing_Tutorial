package basic_java;

//9. Reverse a number

public class ReverseANumber {
    public static void main(String[] args) {
        int num=123;
        int reverse = 0;
        System.out.println("Before Reversal of a number::"+ num);
        while (num !=0) {
            int remainder = num % 10;
            reverse = reverse * 10 + remainder;
            num = num / 10;
        }
        System.out.println("After Reversal of a number::"+ reverse);
    }
}
//Output:
//Before Reversal of a number::123
//After Reversal of a number::321
