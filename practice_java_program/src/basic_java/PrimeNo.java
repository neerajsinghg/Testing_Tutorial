package basic_java;

//8. Prime no generation between 2 numbers.
//
//A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In other words, a prime number is a number that is divisible only by 1 and itself, and has no other factors.
//
//For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, and so on, are prime numbers because they cannot be divided evenly by any other numbers except 1 and themselves.


public class PrimeNo {
    public static void main(String[] args) {
        int first = 10;
        int second = 20;
        for (int i = first; i < second; i++) {
            boolean value = isPrime(i);
            if (value) System.out.println("Prime no::" + i);

        }

    }

    private static boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i < num; i++) {
            if (num % i == 0) return false;
        }

        return true;
    }
}
//output :
//Prime no::11
//Prime no::13
//Prime no::17
//Prime no::19
