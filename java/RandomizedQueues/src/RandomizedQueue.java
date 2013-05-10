import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Created with IntelliJ IDEA.
 * User: Administrator
 * Date: 13-5-10
 * Time: 上午6:50
 * To change this template use File | Settings | File Templates.
 */
public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] q;            // queue elements
    private int N = 0;           // number of elements on queue
    private int first = 0;       // index of first element of queue
    private int last  = 0;       // index of next available slot

    public RandomizedQueue(){
        q = (Item[]) new Object[2];
    }
    public boolean isEmpty()
    {
        return N == 0;
    }
    public int size(){
        return N;
    }

    public void enqueue(Item item){
        if (item == null) throw new NullPointerException();
        if (N == q.length) resize(2*q.length);   // double size of array if necessary
        q[last++] = item;                        // add item
        if (last == q.length) last = 0;          // wrap-around
        N++;
    }

    // resize the underlying array
    private void resize(int max) {
        assert max >= N;
        Item[] temp = (Item[]) new Object[max];
        for (int i = 0; i < N; i++) {
            temp[i] = q[(first + i) % q.length];
        }
        q = temp;
        first = 0;
        last  = N;
    }

    public Item dequeue(){
        if (isEmpty()) throw new NoSuchElementException();
        int index = StdRandom.uniform(first, last);
        Item item = q[index];
        if (last == 0)
            last = q.length - 1;
        else
            last--;
        q[index] = q[last];
        q[last] = null;
        N--;
        return item;
    }

    public Item sample(){
        if (isEmpty()) throw new NoSuchElementException();
        int index = StdRandom.uniform(first, last);
        Item item = q[index];
        return item;
    }

    public Iterator<Item> iterator(){
          return new RandomIterator();
    }

    private class RandomIterator implements Iterator<Item>{
        private int[] indexs;
        private int currentIndex;

        public RandomIterator(){
            indexs = new int[N];
            for (int i = 0; i < N; i++)
            {
                indexs[i] = i;
            }
            StdRandom.shuffle(indexs);

            currentIndex = 0;
        }
        public boolean hasNext(){return currentIndex < N;}
        public void remove(){throw new UnsupportedOperationException();}

        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            int index = (first + indexs[currentIndex]) % q.length;
            Item item = q[index];
            currentIndex++;
            return item;
        }
    }
}
