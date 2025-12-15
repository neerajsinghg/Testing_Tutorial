package java_question;

import java.util.HashMap;

public class RomanNumberToInteger {
    public static void main(String[] args) {
        String input = "VII"; // Example Roman numeral

        // Creating a HashMap to store Roman numeral values
        HashMap<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);

        int result = 0;
        int previousValue = 0;

        // Loop through the string from right to left
        for (int i = input.length() - 1; i >= 0; i--) {
            char currentChar = input.charAt(i);
            int currentValue = romanMap.get(currentChar);

            // If the current value is greater than or equal to the previous value, add it
            if (currentValue >= previousValue) {
                result = result + currentValue;
            } else {
                result = result - currentValue;
            }

            // Update the previous value
            previousValue = currentValue;
        }

        // Print the final result
        System.out.println("Integer value: " + result);
    }
}

