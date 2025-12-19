package basic_java;

//5. Factorial of a number recursively/ iterative way
//
//The factorial of a whole number is the function that multiplies the number by every natural number below it.
//
//n! or “n factorial” means:
//
//n! = 1 · 2 · 3 · … · n = Product of the first n positive integers = n(n-1)(n-2)…………………….(3)(2)(1)
//Example: 5 factorial, that is, 5! can be written as: 5! = 5 × 4 × 3 × 2 × 1 = 120.

public class Factorial {

  // Recursion way
  static int fact(int num) {
      if (num < 0) return -1;
      if (num == 0) return 1;
      else
          return (num * fact(num - 1));

  }

  public static void main(String[] args) {
      //Iterative way
      int fact = 1;
      int num = 5;
      if (num < 0) System.out.println("Factorial cant be calculated for negative no");
      if (num == 0) System.out.println("Factorial of 0 is::" + 1);
      for (int i = 1; i <= num; i++) {
          fact = fact * i;
      }
      System.out.println("Factorial of " + num + " using iterative way " 
      + fact);

      System.out.println("Factorial of " + num + " using recursive way " 
      + fact(num));
  }
}
//output :
//Factorial of 5 using iterative way 120
//Factorial of 5 using recursive way 120 
