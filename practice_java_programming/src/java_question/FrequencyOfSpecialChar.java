/** write a program to count special char;
 * import java.util.HashMap;

public class CountFrequencyOfSpecialChars {
    public static void main(String[] args) {
        String s = "abc@@!!"; // Example input with special characters

        // HashMap to store the frequency of special characters
        HashMap<Character, Integer> frequency = new HashMap<>();

        // Convert string to character array
        char[] inputArray = s.toCharArray();

        // Iterate through each character in the string
        for (char c : inputArray) {
            // Check if character is NOT alphanumeric or space (i.e., special character)
            if (!Character.isLetterOrDigit(c) && c != ' ') {
                // If already present in HashMap, increment count
                frequency.put(c, frequency.getOrDefault(c, 0) + 1);
            }
        }

        // Print the frequency of special characters
        System.out.println("Special Character Frequency: " + frequency);
    }
}

 */
package java_question;

import java.util.HashMap;

public class FrequencyOfSpecialChar {
    public static void main(String[] args) {
        String s = "abc@@!!123$%"; // Example input
        HashMap<Character, Integer> frequency = new HashMap<>();

        char[] inputArray = s.toCharArray(); // Convert string to character array

        for (char c : inputArray) {
            // Check if the character is NOT a letter, digit, or space
            if (!((c >= 'a' && c <= 'z') || 
                  (c >= 'A' && c <= 'Z') || 
                  (c >= '0' && c <= '9') || 
                  (c == ' '))) {
                
                // If already present, increase the count, otherwise initialize to 1
                if (frequency.containsKey(c)) {
                    frequency.put(c, frequency.get(c) + 1);
                } else {
                    frequency.put(c, 1);
                }
            }
        }

        // Print the frequency of special characters
        System.out.println("Special Character Frequency: " + frequency);
    }
}
