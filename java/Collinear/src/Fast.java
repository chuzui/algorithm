import java.util.Arrays;
/**
 * Created with IntelliJ IDEA.
 * User: Administrator
 * Date: 13-5-17
 * Time: 上午12:23
 * To change this template use File | Settings | File Templates.
 */
public class Fast {
    public static void main(String[] args)  {
        String filename = args[0];
        In in = new In(filename);
        int N = in.readInt();
        Point[] points = new Point[N];
        for (int i = 0; i < N; i++) {
            int x = in.readInt();
            int y = in.readInt();
            Point p = new Point(x, y);
            points[i] = p;
        }

        int len = points.length;
        Point[] sortedPoints = new Point[N - 1];
        for (int index = 0; index < len; index++){
            Point p = points[index];
            int sortedIndex = 0;
            for (int i = 0; i < N; i++){
                if (index != i){
                    sortedPoints[sortedIndex] = points[i];
                    sortedIndex ++;
                }
            }
            Arrays.sort(sortedPoints, p.SLOPE_ORDER);
            int i = 0;
            for (int j = 1; j < N - 1; j++){
                if (p.slopeTo(sortedPoints[i]) != p.slopeTo(sortedPoints[j])){
                    if ((j - i) >= 3)
                    {
                        if (sortedPoints[i].compareTo(p) == 1){
                            StdOut.printf("%s -> ", p);
                            for (int m = i; m < j - 1; m++){
                                StdOut.printf("%s -> ", sortedPoints[m]);
                            }
                            StdOut.printf("%s\n", sortedPoints[j - 1]);
                        }
                    }
                    i = j;
                }
            }
        }
    }
}
