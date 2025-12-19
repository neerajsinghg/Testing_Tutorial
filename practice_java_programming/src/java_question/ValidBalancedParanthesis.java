/**write a program to explained paranthesis is balanced or not 
 * 
 */
package java_question;
import java.util.Stack;

public class ValidBalancedParanthesis {
    public static void main(String[] args) {
        String input = "{()}";
        System.out.println("Is valid? " + isValidParenthesis(input));
    }

    public static boolean isValidParenthesis(String input) {
        Stack<Character> stack = new Stack<>();
        
        // Loop through each character in the input string
        for (char currentChar : input.toCharArray()) {
            if (currentChar == '(' || currentChar == '{' || currentChar == '[') {
                stack.push(currentChar); // Push opening bracket to stack
            } else {
                // If stack is empty, no matching opening bracket is present
                if (stack.isEmpty()) {
                    return false;
                }
                
                // Pop the last inserted bracket and check if it matches
                char topChar = stack.pop();
                if (!isMatchingPair(topChar, currentChar)) {
                    return false;
                }
            }
        }

        // If the stack is empty, all brackets were matched correctly
        return stack.isEmpty();
    }

    private static boolean isMatchingPair(char open, char close) {
        return (open == '(' && close == ')') || 
               (open == '{' && close == '}') || 
               (open == '[' && close == ']');
    }
}

