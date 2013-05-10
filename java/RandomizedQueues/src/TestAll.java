import junit.framework.TestCase;

import java.util.Iterator;

/**
 * Created with IntelliJ IDEA.
 * User: Administrator
 * Date: 13-5-10
 * Time: 上午12:27
 * To change this template use File | Settings | File Templates.
 */
public class TestAll extends TestCase {
    public void testDeque(){
        Deque<Integer> a = new Deque<Integer>();
        a.addFirst(5);
        a.addLast(4);
        a.addFirst(3);
        a.removeLast();
        for (Iterator iter = a.iterator(); iter.hasNext();)
        {
             System.out.println(iter.next());
        }
    }
}
