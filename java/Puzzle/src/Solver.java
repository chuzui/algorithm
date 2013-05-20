import java.util.Comparator;

/**
 * Created with IntelliJ IDEA.
 * User: chuzui
 * Date: 5/20/13
 * Time: 4:17 PM
 * To change this template use File | Settings | File Templates.
 */
public class Solver {
    private boolean mIsSolvable;
    private int mMoves;

    public Solver(Board initial){
        MinPQ minPq = new MinPQ(new ManhattanCom());

    }

    public boolean isSolvable(){
        return mIsSolvable;
    }

    public int moves(){
        return mMoves;
    }

    public Iterable<Board> solution(){

    }

    private class BoardBag{

        Board mBoard;
        Board mParent;
        int mMoves;

        public BoardBag(Board board, Board parent, int moves)
        {
            mBoard = board;
            mParent = parent;
            mMoves = moves;
        }
    }

    private class ManhattanCom implements Comparator<BoardBag> {

        public int compare(BoardBag b1, BoardBag b2){
            int value1 = b1.mMoves + b1.mBoard.manhattan();
            int value2 = b2.mMoves + b2.mBoard.manhattan();
            if (value1 < value2) return -1;
            if (value1 > value2) return 1;
            return 0;
        }
    }

    public static void main(String[] args){
        // create initial board from file
        In in = new In(args[0]);
        int N = in.readInt();
        int[][] blocks = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                blocks[i][j] = in.readInt();
        Board initial = new Board(blocks);

        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }
}
