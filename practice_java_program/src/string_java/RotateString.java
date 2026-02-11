package string_java;

public class RotateString {
    public static void main(String[] args) {

        String s = "abcdef";
        int k = 2;

        k = k % s.length();

        String rotated = s.substring(k) + s.substring(0, k);

        System.out.println(rotated);
    }
}