package ch3;

import java.util.Scanner;

/**
 * Created by Administrator on 2014/5/14.
 */
public class InputTest {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);

        System.out.println("What is your name");
        String name = in.nextLine();

        System.out.println("How old are you");
        int age = in.nextInt();

        System.out.println("Hello, " + name + " age " + age);

    }
}
