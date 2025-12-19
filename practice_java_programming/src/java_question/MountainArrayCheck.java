package java_question;

public class MountainArrayCheck {
    public static void main(String[] args) {
        int a[] = {1, 3, 5, 10, 4, 2, 0};

        System.out.println(mountainArrayCheck(a));
    }

    private static boolean mountainArrayCheck(int[] a) {
        // 1. length of the array must be greater than 2
        if (a.length < 3) {
            return false;
        }

        // 2. Elements must be in increasing order!!!
        int i = 0;
        while (i + 1 < a.length && a[i] < a[i + 1]) {
            i++;
        }

        while (i + 1 < a.length && a[i] > a[i + 1]) {
            i++;
        }

        return i == a.length - 1;
    }
}

