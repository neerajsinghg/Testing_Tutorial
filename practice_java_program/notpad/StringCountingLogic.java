public class StringCountingLogic {

    public static void main(String[] args) {

        String input = "aaabbc";     //output="a3b2c1"
        StringBuilder sb = new StringBuilder();

        int count = 1;

        for (int i = 1; i <= input.length(); i++) {

            if (i < input.length() && input.charAt(i) == input.charAt(i - 1)) {
                count++;
            } else {
                sb.append(input.charAt(i - 1)).append(count);
                count = 1;
            }
        }

        System.out.println(sb.toString());
    }
}
