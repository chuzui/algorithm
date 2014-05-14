/**
 * Created by Administrator on 2014/5/13.
 */
public class hello {
    public static void main(String[] args)
    {
        int i, j;
        String[] greeting = new String[3];
        greeting[0] = "welcome";
        greeting[1] = "by";
        greeting[2] = "and";
        for (String g : greeting)
        {
            System.out.println(g);
        }
        System.out.println("java\u2122");
    }

}
