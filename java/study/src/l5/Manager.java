package l5;

import l4.Employee;

import java.util.Date;

/**
 * Created by Administrator on 2014/5/14.
 */
public class Manager extends Employee {
    private int bonus;

    public Manager(String name, double salary, Date hireDay, int bonus) {
        super(name, salary, hireDay);
        this.bonus = bonus;
    }

    public static void main(String[] args)
    {
        Manager m = new Manager("hary", 10000, new Date(), 8000);
        System.out.println(m.getClass().getName());
    }
}
