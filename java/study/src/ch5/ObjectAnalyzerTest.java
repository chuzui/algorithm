package ch5;

import java.util.Date;

/**
 * Created by Administrator on 2014/5/14.
 */
public class ObjectAnalyzerTest {
    public static void main(String[] args)
    {
        Manager m = new Manager("hary", 10000, new Date(), 8000);
        System.out.print(new ObjectAnalyzer().toString(m));
    }
}
