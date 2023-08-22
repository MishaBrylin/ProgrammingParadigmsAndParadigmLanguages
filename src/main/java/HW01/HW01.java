


package HW01;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
//Императивное программирование:
//        Задача 1: Подсчет суммы четных чисел от 1 до N.
//        Напишите программу, используя цикл, которая находит сумму всех четных чисел в диапазоне от 1 до заданного числа N.
public class HW01 {
    public static Integer sumEven(int n){
        int sum = 0;
        for(int i = 0; i < n+1; i++){
            if (i%2 == 0){
                sum+=i;
            }
        }
        return sum;

    }

//Императивное программирование:
//        Задача 2: Поиск наименьшего числа в списке.
//        Напишите программу, которая находит наименьшее число в заданном списке с помощью цикла.
    public static Integer minNumber(List<Integer> list){
        int min = list.get(0);
        for(int i = 0; i < list.size(); i++){
            if (min > list.get(i)){
                min = list.get(i);
            }

        }
        return min;
    }
    //        Декларативное программирование:
//        Задача 3: Вычисление факториала числа.
//        Напишите программу, которая находит факториал заданного числа N с использованием рекурсии или встроенных функций.
    public static long calculateFactorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * calculateFactorial(n - 1);
        }
    }


    public static void main(String[] args) {

        System.out.println(sumEven(6));
        List<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(12);
        list.add(2);
        System.out.println(minNumber(list));
        System.out.println(calculateFactorial(8));
//        Декларативное программирование:
//        Задача 4: Поиск уникальных элементов в списке.
//        Напишите программу, которая создает новый список, содержащий только уникальные элементы из исходного списка.
        System.out.println(Arrays.asList(1, 2, 3, 2, 4, 3, 5, 1, 6, 7, 7, 6, 8, 9).stream().distinct().collect(Collectors.toList()));

    }
}
