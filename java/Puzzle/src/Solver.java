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
    private Stack<Board> solveStack = null;

    public Solver(Board initial){
        MinPQ initMinPq = new MinPQ(new ManhattanCom());
        MinPQ twinMinPq = new MinPQ(new ManhattanCom());

        Board twinBoard = initial.twin();

        BoardBag initBag = new BoardBag(initial, null, 0);
        BoardBag twinBag = new BoardBag(twinBoard, null, 0);

        initMinPq.insert(initBag);
        twinMinPq.insert(twinBag);

        SET<BoardBag> initVisitedSet = new SET<BoardBag>();
        SET<BoardBag> twinVisitedSet = new SET<BoardBag>();
        initVisitedSet.add(initBag);
        twinVisitedSet.add(twinBag);

        BoardBag goal = null;
        int moves = -1;

        while (true){

            if (!initMinPq.isEmpty()){
                BoardBag currentBoardBag = (BoardBag)initMinPq.delMin();
                if (currentBoardBag.mBoard.isGoal()){
                    mIsSolvable = true;
                    goal = currentBoardBag;
                    break;
                }
                else{
                    for (Board board: currentBoardBag.mBoard.neighbors()){
                        BoardBag nextBag = new BoardBag(board, currentBoardBag, currentBoardBag.mMoves + 1);
                        if (!initVisitedSet.contains(nextBag)){
                            initMinPq.insert(nextBag);
                            initVisitedSet.add(nextBag);
                        }
                    }
                }
            }

            if (!twinMinPq.isEmpty()){
                BoardBag currentBoardBag = (BoardBag)twinMinPq.delMin();
                twinVisitedSet.add(currentBoardBag);
                if (currentBoardBag.mBoard.isGoal()){
                    mIsSolvable = false;
                    mMoves = -1;
                    break;
                }
                else{
                    for (Board board: currentBoardBag.mBoard.neighbors()){
                        BoardBag nextBag = new BoardBag(board, currentBoardBag, currentBoardBag.mMoves + 1);
                        if (!twinVisitedSet.contains(nextBag)){
                            twinMinPq.insert(nextBag);
                            twinVisitedSet.add(nextBag);
                        }
                    }
                }
            }

        }

        if (isSolvable()){
            solveStack = new Stack<Board>();
            while (goal != null){
                solveStack.push(goal.mBoard);
                goal = goal.mParent;
                moves += 1;
            }
            mMoves = moves;
        }
    }

    public boolean isSolvable(){
        return mIsSolvable;
    }

    public int moves(){
        return mMoves;
    }

    public Iterable<Board> solution(){
         return solveStack;
    }

    private class BoardBag implements Comparable<BoardBag>{

        Board mBoard;
        BoardBag mParent;
        int mMoves;

        public BoardBag(Board board, BoardBag parent, int moves)
        {
            mBoard = board;
            mParent = parent;
            mMoves = moves;
        }

        public int compareTo(BoardBag y){
            if (this.mBoard.equals(y.mBoard))
                 return 0;
            if (this.mBoard.manhattan() > y.mBoard.manhattan())
                return 1;
            else
                return -1;
        }

        public int hashCode(){
            int hash = 17;
            int N = mBoard.dimension();
            hash = mBoard.hamming() * 65535 + mBoard.manhattan() + hash;
            return hash;
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
