/**
 * Created with IntelliJ IDEA.
 * User: chuzui
 * Date: 13-5-6
 * Time: 上午10:52
 * To change this template use File | Settings | File Templates.
 */
public class PercolationStats {
    private double openSites[];
    // perform T independent computational experiments on an N-by-N grid
    public PercolationStats(int N, int T){
        if (N <= 0 || T <= 0)
            throw new IllegalArgumentException();
        openSites = new double[T];
        for (int k = 0; k < T; k++)
        {
            int openSiteCount = 0;
            Percolation percolation = new Percolation(N);
            while (!percolation.percolates()){
                int i = StdRandom.uniform(N) + 1;
                int j = StdRandom.uniform(N) + 1;
                if (!percolation.isOpen(i, j)){
                    percolation.open(i, j);
                    openSiteCount += 1;
                }
            }
            openSites[k] = (double)openSiteCount / (N*N);
        }
    }

    // sample mean of percolation threshold
    public double mean(){
         return StdStats.mean(openSites);
    }

    // sample standard deviation of percolation threshold
    public double stddev()
    {
        return StdStats.stddev(openSites);
    }

    // returns lower bound of the 95% confidence interval
    public double confidenceLo(){
        return mean() - 1.96 * Math.sqrt(stddev()) / openSites.length;
    }

    // returns upper bound of the 95% confidence interval
    public double confidenceHi()
    {
        return mean() + 1.96 * Math.sqrt(stddev()) / openSites.length;
    }

    // test client, described below
    public static void main(String[] args){
        int N = Integer.parseInt(args[0]);
        int T = Integer.parseInt(args[1]);
        PercolationStats p = new PercolationStats(N, T);
        System.out.printf("%-24s= %f", "mean", p.mean());
        System.out.printf("%-24s= %f", "stddev", p.stddev());
        System.out.printf("%-24s= %f, %f", "95% confidence interval", p.confidenceLo(), p.confidenceHi());
    }
}
