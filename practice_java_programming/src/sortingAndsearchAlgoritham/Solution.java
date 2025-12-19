package src.sortingAndsearchAlgoritham;

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // Convert int to String
        String s = Integer.toString(n);

        // Now check if the conversion is correct
        if (n == Integer.parseInt(s)) {
            System.out.println("Good job");
        } else {
            System.out.println("Wrong answer");
        }

        sc.close();
    }
}

