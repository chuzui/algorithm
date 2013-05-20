import java.util.Arrays
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

        for (Point p: points){
            Point[] sortedPoints = points.clone();
            Arrays.sort(sortedPoints, p.SLOPE_ORDER);
            int i = 0;
            for (int j = 1; j < N; j++){

            }
        }
    }
}
