package ch12;

import java.io.File;
import java.util.Scanner;

/**
 * Created by Administrator on 2014/5/16.
 */

public class BlockTest {
    public static void main(String[] args)
    {
        new Block()
        {
            public void body() throws Exception
            {
                Scanner in = new Scanner(new File("quq"));
                while (in.hasNext())
                    System.out.print(in.next());
            }
        }.toThread().start();
    }
}

abstract class Block
{
    public abstract void body() throws Exception;

    public Thread toThread()
    {
        return new Thread()
        {
            public void run()
            {
                try
                {
                    body();
                }
                catch (Throwable t)
                {
                    //t.printStackTrace();
                    Block.<RuntimeException>throwAs(t);
                }
            }
        };
    }

    @SuppressWarnings("unchecked")
    public static <T extends Throwable> void throwAs(Throwable e) throws T
    {
        throw (T) e;
    }
}
