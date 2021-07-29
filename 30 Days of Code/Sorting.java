import java.util.Scanner;
public class Sorting {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[] = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = in.nextInt();
        }
        in.close();
        int count = 0;
        for (int j = a.length - 1;j >= 0; j--) {
            for (int k = 0; k < j; k++) {

                if (a[k] > a[k + 1]) {
                    int temp = a[k];
                    count++;
                    a[k] = a[k + 1];
                    a[k + 1] = temp;
                }
            }
        }
        System.out.println("Array is sorted in " + count + " swaps.");
        System.out.println("First Element: " + a[0]);
        System.out.println("Last Element: " + a[a.length - 1]);

    }
}
