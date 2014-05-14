package l4;


import java.util.Date;

/**
 * Created by Administrator on 2014/5/14.
 */
public class Employee {
    private String name;
    private double salary;
    private Date hireDay;

    public Employee(String name, double salary, Date hireDay) {
        this.name = name;
        this.salary = salary;
        this.hireDay = hireDay;
    }

    public void print()
    {
        int i = 5;
        int a = 6+7+8+9;
        int b = 7+i;
    }

    public Date getHireDay() {
        return (Date) hireDay.clone();
    }
}
