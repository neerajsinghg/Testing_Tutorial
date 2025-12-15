package smartpractice;

import java.util.Random;

public class RandomEmailGenerator {

    public static void main(String[] args) {
        // Define characters allowed in username
        String characters = "abcdefghijklmnopqrstuvwxyz1234567890";
        String domain = "@example.com"; // You can change this domain
        StringBuilder emailPrefix = new StringBuilder();

        Random random = new Random();
        int length = 8; // Length of username part of email

        // Generate random string
        for (int i = 0; i < length; i++) {
            int index = random.nextInt(characters.length());
            emailPrefix.append(characters.charAt(index));
        }

        // Combine username and domain
        String randomEmail = emailPrefix.toString() + domain;

        // Print the result
        System.out.println("Generated Random Email ID: " + randomEmail);
    }
}

