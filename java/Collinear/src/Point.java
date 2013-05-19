/*************************************************************************
 * Name:
 * Email:
 *
 * Compilation:  javac Point.java
 * Execution:
 * Dependencies: StdDraw.java
 *
 * Description: An immutable data type for points in the plane.
 *
 *************************************************************************/

import java.util.Comparator;

public class Point implements Comparable<Point> {

    // compare points by slope
    public final Comparator<Point> SLOPE_ORDER = new BySlope(this);

    private class BySlope implements Comparator<Point>{
        private Point p0;

        public BySlope(Point p0){
            this.p0 = p0;
        }
        public int compare(Point p1, Point p2){
            double slopeP1, slopep2;
            slopeP1 = p0.slopeTo(p1);
            slopep2 = p0.slopeTo(p2);
            if (slopeP1 < slopep2) return -1;
            if (slopeP1 > slopep2) return 1;
            return 0;
        }
    }

    private final int x;                              // x coordinate
    private final int y;                              // y coordinate

    // create the point (x, y)
    public Point(int x, int y) {
        /* DO NOT MODIFY */
        this.x = x;
        this.y = y;
    }

    // plot this point to standard drawing
    public void draw() {
        /* DO NOT MODIFY */
        StdDraw.point(x, y);
    }

    // draw line between this point and that point to standard drawing
    public void drawTo(Point that) {
        /* DO NOT MODIFY */
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    // slope between this point and that point
    public double slopeTo(Point that) {
        if (this.x == that.x){
            if (this.y == that.y){
                return 0.0 / 1.0;
            }
            return Double.POSITIVE_INFINITY;
        }
        return (((double)that.y - this.y) / (that.x - this.x));
    }

    // is this point lexicographically smaller than that one?
    // comparing y-coordinates and breaking ties by x-coordinates
    public int compareTo(Point that) {
        if (this.y < that.y)
            return -1;
        else if (this.y > that.y)
            return 1;

        if (this.x < that.x)
            return -1;
        else if (this.x > that.x)
            return 1;
        return 0;
    }

    // return string representation of this point
    public String toString() {
        /* DO NOT MODIFY */
        return "(" + x + ", " + y + ")";
    }

    // unit test
    public static void main(String[] args) {
        /* YOUR CODE HERE */
    }
}
