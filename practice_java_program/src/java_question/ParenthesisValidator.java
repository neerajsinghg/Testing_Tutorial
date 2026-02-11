package java_question;

import java.util.Stack;

public class ParenthesisValidator {

    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {

            // push opening brackets
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }
            // handle closing brackets
            else {
                if (stack.isEmpty())
                    return false;

                char top = stack.pop();

                if ((ch == ')' && top != '(') ||
                    (ch == '}' && top != '{') ||
                    (ch == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        System.out.println(isValid("(){}[]"));     // true
        System.out.println(isValid("([{}])"));     // true
        System.out.println(isValid("(]"));         // false
        System.out.println(isValid("((("));        // false
    }
}

