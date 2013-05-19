/**
 * Created with IntelliJ IDEA.
 * User: Administrator
 * Date: 13-5-17
 * Time: 上午12:23
 * To change this template use File | Settings | File Templates.
 */
public class Brute {
    public static void main(String[] args) {
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

        for (int i = 0; i < N-3; i++)
            for (int j = i + 1; j < N - 2; j++ )
                for (int k = j + 1; k < N - 1; k++)
                    for (int m = k + 1; m < N; m++){
                        double slope1 = points[i].slopeTo(points[j]);
                        double slope2 = points[i].slopeTo(points[k]);
                        double slope3 = points[i].slopeTo(points[m]);
                        if (slope1 == slope2 && slope1 == slope3)
                            StdOut.printf("%s -> %s -> %s -> %s\n", points[i], points[j], points[k], points[m]);
                    }
    }
}
