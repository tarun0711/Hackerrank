import java.util.*;
public class Candies
{
  static long candies(int n, int[] arr)
  {

  int[] candies = new int[n];
  candies[0] = 1;
  for (int i = 1; i < n; i++) {
    if (arr[i] > arr[i - 1]) {
      candies[i] = candies[i - 1] + 1;
    } else {
      candies[i] = 1;
    }
  }

  for (int i = n - 2; i >= 0; i--) {
    if (arr[i] > arr[i + 1] && candies[i] <= candies[i + 1]) {
      candies[i] = candies[i + 1] + 1;
    }
  }

  long sum = 0;
  for (int c : candies) {
    sum += c;
  }
  return sum;
}
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int A[] = new int[n];
        for(int i=0;i<n;i++)
        {
            A[i]= sc.nextInt();
        }
       
        long s = candies(n,A);
        System.out.println(s);
    }
}
