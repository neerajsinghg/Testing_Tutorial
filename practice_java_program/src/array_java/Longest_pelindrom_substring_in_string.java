package array_java;

class Longest_pelindrom_substring_in_string {

    static String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }

        String result = "";  // final answer store karega
        int n = s.length();

        for (int i = 0; i < n; i++) {

            // Case 1: Odd length palindrome (center i pe)
            int l = i, r = i;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > result.length()) {
                    result = s.substring(l, r + 1);
                }
                l--;
                r++;
            }

            // Case 2: Even length palindrome (center i aur i+1 ke beech)
            l = i;
            r = i + 1;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > result.length()) {
                    result = s.substring(l, r + 1);
                }
                l--;
                r++;
            }
        }

        return result;
    }

    // Test cases
    public static void main(String[] args) {
        String[] testCases = {
            "mississippi",
            "avcccvbgf",
            "abcdc",
            "a",
            "abc"
        };

        for (String s : testCases) {
            System.out.println("String: " + s +
                    " -> Longest Palindrome: " + longestPalindrome(s));
        }
    }
}

