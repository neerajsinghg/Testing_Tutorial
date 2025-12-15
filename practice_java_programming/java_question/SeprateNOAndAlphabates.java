/*
 * write a program to separate numbers and alphabets
 */
package java_question;

public class SeprateNOAndAlphabates {
    public static void main(String[] args) {
        String input = "Ra123"; // Example input

        // StringBuilder to store numbers and alphabets separately
        StringBuilder numbers = new StringBuilder();
        StringBuilder alphabets = new StringBuilder();

        // Iterate through each character in the string
        for (char currentChar : input.toCharArray()) {
            if (Character.isDigit(currentChar)) {
                numbers.append(currentChar); // Append digits to numbers
            } else if (Character.isAlphabetic(currentChar)) {
                alphabets.append(currentChar); // Append alphabets to alphabets
            }
        }

        // Print the separated alphabets and numbers
        System.out.println(alphabets.toString());
        System.out.println(numbers.toString());
    }
}

