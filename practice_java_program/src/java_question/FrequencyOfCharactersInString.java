/**
 * write a program to find frequency  of character  
 */
package java_question;

import java.util.HashMap;

public class FrequencyOfCharactersInString {
    public static void main(String[] args) {
        String input = "madam";

        // Creating a HashMap to store character frequency
        HashMap<Character, Integer> frequencyMap = new HashMap<>();

        // Convert the String to a character array
        char[] inputArray = input.toCharArray();

        // Traverse this char array
        for (char character : inputArray) {
            // Update the frequency map
            frequencyMap.put(character, frequencyMap.getOrDefault(character, 0) + 1);
        }

        // Print character frequencies
        for (char c : frequencyMap.keySet()) {
            System.out.println(c + " -> " + frequencyMap.get(c));
        }
    }
}

