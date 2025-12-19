/*
 * write the program to count the number in the changing key in given string
 */
package java_question;

public class ChangingKeys {
    public static void main(String[] args) {
        String input = "aBbC"; // Example input
        int count = 0;

        // Convert the string to lowercase and get the first character
        char lastKey = input.toLowerCase().toCharArray()[0];
        lastKey = Character.toLowerCase(lastKey);

        System.out.println(lastKey); // Print the first key

        // Iterate through the string and count key changes
        for (int i = 1; i < input.length(); i++) {
            char currentKey = input.toCharArray()[i];
            currentKey = Character.toLowerCase(currentKey);

            if (currentKey != lastKey) { 
                count++; // Increment count when key changes
            }
            lastKey = currentKey; // Update last key
        }

        System.out.println("The total Number of Keys changed is " + count);
    }
}

