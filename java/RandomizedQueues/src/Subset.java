/**
 * Created with IntelliJ IDEA.
 * User: Administrator
 * Date: 13-5-10
 * Time: 上午7:31
 * To change this template use File | Settings | File Templates.
 */
public class Subset {
    public static void main(String[] args){
        int k = Integer.parseInt(args[0]);

        RandomizedQueue<String> randomQueue = new RandomizedQueue<String>();
        String s = null;
        while(!StdIn.isEmpty())
        {
            s = StdIn.readString();
            randomQueue.enqueue(s);
        }

        for (int i = 0; i < k; i++)
        {
            StdOut.println(randomQueue.dequeue());
        }
    }
}
