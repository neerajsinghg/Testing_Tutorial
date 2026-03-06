public class PossibleStringCombinations{

    public static void main(String[] args) {
        String str = "ABC";
        combine(str, "", 0);
    }

    public static void combine(String str, String result, int index) {

        if (index == str.length()) {
            if (!result.isEmpty()) {
                System.out.println(result);
            }
            return;
        }

        // Include current character
        combine(str, result + str.charAt(index), index + 1);

        // Exclude current character
        combine(str, result, index + 1);
    }
}
