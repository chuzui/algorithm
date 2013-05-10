import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Created with IntelliJ IDEA.
 * User: Administrator
 * Date: 13-5-9
 * Time: 下午11:47
 * To change this template use File | Settings | File Templates.
 */
public class Deque<Item> implements Iterable<Item> {
    private int N;         // number of elements on queue
    private Node first;    // beginning of queue
    private Node last;     // end of queue

    // helper linked list class
    private class Node {
        private Item item;
        private Node next;
        private Node prev;
    }

    public Deque(){
        first = null;
        last = null;
        N = 0;
    }

    public boolean isEmpty(){
        return N == 0;
    }
    public int size(){
        return N;
    }

    public void addFirst(Item item)
    {
        if (item == null) throw new NullPointerException();
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.prev = null;
        first.next = oldfirst;
        if (isEmpty()) last = first;
        else oldfirst.prev = first;
        N++;
    }

    public void addLast(Item item){
        if (item == null) throw new NullPointerException();
        Node oldlast = last;
        last = new Node();
        last.item = item;
        last.next = null;
        last.prev = null;
        if (isEmpty()) first = last;
        else {
            oldlast.next = last;
            last.prev = oldlast;
        }
        N++;
    }
    public Item removeFirst(){
        if (isEmpty()) throw new NoSuchElementException();
        Item item = first.item;
        first = first.next;
        N--;
        if (isEmpty()) last = null;
        else first.prev = null;
        return item;
    }
    public Item removeLast(){
        if (isEmpty()) throw new NoSuchElementException();
        Item item = last.item;
        last = last.prev;
        N--;
        if (isEmpty()) first = null;
        else last.next = null;
        return item;
    }

    public Iterator<Item> iterator(){
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext()  { return current != null;                     }
        public void remove()      { throw new UnsupportedOperationException();  }

        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }
}
