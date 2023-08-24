package HW02;

import java.util.*;

public class ArraySplitter {
    public static List<List<Integer>> splitArray(int[] arr, int x) {
        List<List<Integer>> subArrays = new ArrayList<>();
        List<Integer> subArray = new ArrayList<>();
        int sum = 0;

        for (int num : arr) {
            if (sum + num > x) {
                subArrays.add(subArray);
                subArray = new ArrayList<>();
                sum = 0;
            }

            subArray.add(num);
            sum += num;
        }

        if (!subArray.isEmpty()) {
            subArrays.add(subArray);
        }

        return subArrays;
    }

    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int x = 15;

        List<List<Integer>> subArrays = splitArray(numbers, x);
        for (List<Integer> subArray : subArrays) {
            System.out.println(subArray);
        }
    }
}
