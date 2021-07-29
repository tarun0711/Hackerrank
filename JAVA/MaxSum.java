import java.math.*;
import java.util.*;


public class MaxSum {

      static int maxSubsetSum(int[] arr)
    {
        int [] result = new int [arr.length];
        result [0] = arr[0];
        result[1] = arr[1]>result[0]?arr[1]:result[0];
        
        for(int i =2; i<arr.length; i++)
        {
            result[i] = Math.max(arr[i]+result[i-2],Math.max(arr[i],Math.max(result[i-1],result[i-2])));
        }
        
        return(result[result.length-1]);


    }


    public static void main(String[] args)
    {
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter n");
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        System.out.println("Enter elements");

        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        int res = maxSubsetSum(arr);
        System.out.println(res);
        scanner.close();
    }
}
