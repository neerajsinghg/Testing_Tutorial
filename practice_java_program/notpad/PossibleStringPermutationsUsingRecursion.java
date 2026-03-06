public class PossibleStringPermutationsUsingRecursion{

    public static void main(String[] args) {
        String str = "ABC";
        permute(str, "");
    }

    public static void permute(String str, String result) {

        // Base case
        if (str.length() == 0) {
            System.out.println(result);
            return;
        }

        for (int i = 0; i < str.length(); i++) {

            char current = str.charAt(i);

            // Remaining string after removing current character
            String remaining = str.substring(0, i) + str.substring(i + 1);

            // Recursive call
            permute(remaining, result + current);
        }
    }
}
