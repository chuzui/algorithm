/**
 * Created with IntelliJ IDEA.
 * User: chuzui
 * Date: 13-5-6
 * Time: 上午10:49
 * To change this template use File | Settings | File Templates.
 */
public class Percolation {
    // create N-by-N grid, with all sites blocked
    private int m_N;
    private WeightedQuickUnionUF union;
    private boolean openState[][];

    public Percolation(int N){
        this.m_N = N;
        union = new WeightedQuickUnionUF(N * N + 2);
        openState = new boolean[N+1][N+1];
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= N; j++)
            {
                openState[i][j] = false;
            }
        }
    }

    // open site (row i, column j) if it is not already
    public void open(int i, int j){
        indexCheck(i, j);
        openState[i][j] = true;
        if (i == 1)
            union.union(coord2index(i, j), 0);

        if (i > 1)
            if (isOpen(i-1, j))
                union.union(coord2index(i, j), coord2index(i-1, j));

        if (i < m_N)
            if (isOpen(i+1, j))
                union.union(coord2index(i, j), coord2index(i+1, j));

        if (j > 1)
            if (isOpen(i, j-1))
                union.union(coord2index(i, j), coord2index(i, j-1));

        if (j < m_N)
            if (isOpen(i, j+1))
                union.union(coord2index(i, j), coord2index(i, j+1));

        if (i == m_N && isFull(i, j))
            union.union(coord2index(i, j), m_N * m_N + 1);
    }

    // is site (row i, column j) open?
    public boolean isOpen(int i, int j){
        indexCheck(i, j);
        return openState[i][j];
    }

    // is site (row i, column j) full?
    public boolean isFull(int i, int j)
    {
        indexCheck(i, j);
        return union.connected(coord2index(i, j), 0) ;
    }

    public boolean percolates()
    {
        return union.connected(0, m_N * m_N + 1);
    }

    private void indexCheck(int i, int j){
        if (i < 1 || i > m_N || j < 1 || j > m_N)
            throw new IndexOutOfBoundsException("index out of bounds");
    }

    private int coord2index(int i, int j)
    {
          return (i - 1) * m_N + j;
    }
}