package java_question;

public class ReplaceVowelWithX {
    public static void main(String[] args) {
        String input = "Name"; // Example input
        StringBuilder result = new StringBuilder();

        // Iterate through each character in the string
        for (char currentChar : input.toCharArray()) {
            if (isVowel(currentChar)) {
                result.append('X'); // Replace vowels with 'X'
            } else {
                result.append(currentChar); // Keep consonants unchanged
            }
        }

        // Print the modified string
        System.out.println(result.toString());
    }

    // Method to check if a character is a vowel
    public static boolean isVowel(char currentChar) {
        if (currentChar == 'a' || currentChar == 'e' || currentChar == 'i' || currentChar == 'o' || currentChar == 'u' ||
            currentChar == 'A' || currentChar == 'E' || currentChar == 'I' || currentChar == 'O' || currentChar == 'U') {
            return true; // Return true if it's a vowel
        }
        return false; // Otherwise, return false
    }
}

