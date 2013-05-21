
/**
 * Created with IntelliJ IDEA.
 * User: chuzui
 * Date: 5/20/13
 * Time: 4:17 PM
 * To change this template use File | Settings | File Templates.
 */
public class Board {
    private int N;
    private int[][] mBlocks;
    private int mManhattan;

    // construct a board from an N-by-N array of blocks
    public Board(int[][] blocks){
       N = blocks.length;
       mBlocks = new int[N][N];
       for (int row = 0; row < N; row++)
           for (int col = 0; col < N; col++)
               mBlocks[row][col] = blocks[row][col];

       mManhattan = -1;
    }

    // board dimension N
    public int dimension(){
        return N;
    }

    // number of blocks out of place
    public int hamming(){
        int hamm = 0;
        for (int row = 0; row < N; row++){
            for (int col = 0; col < N; col++){
                if (mBlocks[row][col] !=0 && mBlocks[row][col] != (row * N + col + 1))
                    hamm += 1;
            }
        }
        return hamm;
    }

    public int manhattan(){
        if (mManhattan != -1) return mManhattan;
        int man = 0;
        for (int row = 0; row < N; row++){
            for (int col = 0; col < N; col++){
                if (mBlocks[row][col] !=0){
                    int goalRow = (mBlocks[row][col] - 1) / N;
                    int goalCol = (mBlocks[row][col] - 1) % N;
                    man += abs(row - goalRow) + abs(col - goalCol);
                }
            }
        }
        mManhattan = man;
        return mManhattan;
    }

    public boolean isGoal(){
        return hamming() == 0;
    }

    public Board twin(){
        int[][] newBlocks = new int[N][N];
        for (int row = 0; row < N; row++)
            for (int col = 0; col < N; col++)
                newBlocks[row][col] = (int)mBlocks[row][col];

        for (int row = 0; row < N; row++){
            if (newBlocks[row][0] != 0 && newBlocks[row][1] != 0){
                int temp = newBlocks[row][0];
                newBlocks[row][0] = newBlocks[row][1];
                newBlocks[row][1] = temp;
                break;
            }
        }

        return new Board(newBlocks);
    }

    public boolean equals(Object y){
        if (y == this) return true;
        if (y == null) return false;
        if (y.getClass() != this.getClass()) return false;
        Board that = (Board) y;
        if (this.N != that.N || this.manhattan() != that.manhattan()) return false;
        for (int row = 0; row < N; row++)
            for (int col = 0; col < N; col++)
                if (this.mBlocks[col][row] != that.mBlocks[row][col])
                    return false;
        return true;
    }

    public Iterable<Board> neighbors(){
        Queue<Board> iter = new Queue<Board>();
        for (int row = 0; row < N; row++)
            for (int col = 0; col < N; col++)
                if (mBlocks[row][col] == 0){
                    if (row > 0)
                        iter.enqueue(exchange(row, col, row - 1, col));
                    if (col > 0)
                        iter.enqueue(exchange(row, col, row, col - 1));
                    if (row < N - 1)
                        iter.enqueue(exchange(row, col, row + 1, col));
                    if (col < N - 1)
                        iter.enqueue(exchange(row, col, row, col + 1));
                }
        return iter;
    }

    public String toString(){
        StringBuilder s = new StringBuilder();
        s.append(N + "\n");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                s.append(String.format("%2d ", mBlocks[i][j]));
            }
            s.append("\n");
        }
        return s.toString();
    }

    private final int abs(int n){
        if (n >= 0)
            return n;
        return -n;
    }

    private final Board exchange(int oldRow, int oldCol, int newRow, int newCol){
        int[][] newBlocks = new int[N][N];
        for (int row = 0; row < N; row++)
            for (int col = 0; col < N; col++)
                newBlocks[row][col] = mBlocks[row][col];

        int temp = newBlocks[oldRow][oldCol];
        newBlocks[oldRow][oldCol] = newBlocks[newRow][newCol];
        newBlocks[newRow][newCol] = temp;
        return new Board(newBlocks);
    }
}

