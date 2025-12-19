/*
 * write a program to find first and last occurence of a char;
 */
package java_question;

public class FirstAndLastOccurrence {
    public static void main(String[] args) {
        String input = "Hello World";  // Input string
        char target = 'o';             // Character to find
        int firstIndex = -1;
        int lastIndex = -1;

        // Find the first occurrence
        for (int index = 0; index < input.length(); index++) {
            if (input.charAt(index) == target) {
                firstIndex = index;
                break;
            }
        }

        // Find the last occurrence
        for (int index = input.length() - 1; index >= 0; index--) {
            if (input.charAt(index) == target) {
                lastIndex = index;
                break;
            }
        }

        // Display the results
        if (firstIndex < 0) {
            System.out.println("Character is not present");
        } else {
            System.out.println("First Occurrence: " + firstIndex);
            System.out.println("Last Occurrence: " + lastIndex);
        }
    }
}
