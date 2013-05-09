
public class SAP {
	
    private boolean[] vmarked;  
    private boolean[] wmarked;
    private int[] vedgeTo;      
    private int[] wedgeTo;      
    private int[] vdistTo;      
    private int[] wdistTo;
	private Digraph G;
	
	// constructor takes a digraph
	public SAP(Digraph G)
	{
		this.G = new Digraph(G);
		vmarked = new boolean[G.V()];
		wmarked = new boolean[G.V()];
		vedgeTo = new int[G.V()];
		vdistTo = new int[G.V()];
		wedgeTo = new int[G.V()];
        wdistTo = new int[G.V()];      
        //for (int v = 0; v < G.V(); v++) distTo[v] = INFINITY;
	}
	
	// length of shortest ancestral path between v and w; -1 if no such path
	public int length(int v, int w)
	{
		if (!isInBound(v) || !isInBound(w))
			throw new IndexOutOfBoundsException();
		int ancestor = getAncestor(v, w);
		if (ancestor == -1)
			return -1;
		return vdistTo[ancestor] + wdistTo[ancestor];
	}
	
	public int ancestor(int v, int w)
	{
		if (!isInBound(v) || !isInBound(w))
			throw new IndexOutOfBoundsException();
		return getAncestor(v, w);
	}
	
	public int length(Iterable<Integer> v, Iterable<Integer> w)
	{
		for (int i : v)
		{
			if (!isInBound(i))
				throw new IndexOutOfBoundsException();
		}
		
		for (int i : w)
		{
			if (!isInBound(i))
				throw new IndexOutOfBoundsException();
		}
		int ancestor = getAncestor(v, w);
		if (ancestor == -1)
			return -1;
		return vdistTo[ancestor] + wdistTo[ancestor];
	}
	
	public int ancestor(Iterable<Integer> v, Iterable<Integer> w)
	{
		for (int i : v)
		{
			if (!isInBound(i))
				throw new IndexOutOfBoundsException();
		}
		
		for (int i : w)
		{
			if (!isInBound(i))
				throw new IndexOutOfBoundsException();
		}
		int ancestor = getAncestor(v, w);
		if (ancestor == -1)
			return -1;
		return ancestor;
	}
	
	private boolean isInBound(int index)
	{
		return (index >=0 && (index < G.V()));
	}
	
	private int getAncestor(int v, int w)
	{
		for (int i = 0; i < G.V(); i++)
		{
			vmarked[i] = false;
			wmarked[i] = false;
		}
		Queue<Integer> vQueue = new Queue<Integer>();
		Queue<Integer> wQueue = new Queue<Integer>();
		vmarked[v] = true;
		wmarked[w] = true;
		vdistTo[v] = 0;
		wdistTo[w] = 0;
		
		vQueue.enqueue(v);
		wQueue.enqueue(w);
		if (v == w)
			return v;
		
		int minLength = Integer.MAX_VALUE;
		int ancestor = -1;
		while (true)
		{
			if (vQueue.isEmpty() && wQueue.isEmpty())
				break;
			int mark = 0;
			if (!vQueue.isEmpty())
			{
				int currentIndex = vQueue.dequeue();
				if (vdistTo[currentIndex] < minLength)
				{
					mark += 1;
					for (int nextindex : G.adj(currentIndex)) {
		                if (!vmarked[nextindex]) {
		                    vedgeTo[nextindex] = currentIndex;
		                    vdistTo[nextindex] = vdistTo[currentIndex] + 1;
		                    vmarked[nextindex] = true;
		                    vQueue.enqueue(nextindex);
		                    if (wmarked[nextindex] == true)
		                    	if ((vdistTo[nextindex] + wdistTo[nextindex]) < minLength)
		                    	{
		                    		ancestor = nextindex;
		                    		minLength = vdistTo[nextindex] + wdistTo[nextindex];
		                    	}	                    			                    		
		                }
		            }
				}          
			}
			
			if (!wQueue.isEmpty())
			{
				int currentIndex = wQueue.dequeue();
				if (wdistTo[currentIndex] < minLength)
				{
					mark += 1;
					for (int nextindex : G.adj(currentIndex)) {
		                if (!wmarked[nextindex]) {
		                    wedgeTo[nextindex] = currentIndex;
		                    wdistTo[nextindex] = wdistTo[currentIndex] + 1;
		                    wmarked[nextindex] = true;
		                    wQueue.enqueue(nextindex);
		                    if (vmarked[nextindex] == true)
		                    	if ((vdistTo[nextindex] + wdistTo[nextindex]) < minLength)
		                    	{
		                    		ancestor = nextindex;
		                    		minLength = vdistTo[nextindex] + wdistTo[nextindex];
		                    	}	                    			                    		
		                }
		            }
				}          
			}
			
			if (mark == 0)
				break;
		}
		return ancestor;
	}
	
	private int getAncestor(Iterable<Integer> v, Iterable<Integer> w)
	{
		for (int i = 0; i < G.V(); i++)
		{
			vmarked[i] = false;
			wmarked[i] = false;
		}
		Queue<Integer> vQueue = new Queue<Integer>();
		Queue<Integer> wQueue = new Queue<Integer>();
		for (int i : v)
		{
			vmarked[i] = true;
			vdistTo[i] = 0;
			vQueue.enqueue(i);
		}
			
		for (int i : w)
		{
			wmarked[i] = true;
			wdistTo[i] = 0;
			wQueue.enqueue(i);
			if (vmarked[i] == true)
				return i;
		}
			
		int minLength = Integer.MAX_VALUE;
		int ancestor = -1;
		while (true)
		{
			if (vQueue.isEmpty() && wQueue.isEmpty())
				break;
			int mark = 0;
			if (!vQueue.isEmpty())
			{
				int currentIndex = vQueue.dequeue();
				if (vdistTo[currentIndex] < minLength)
				{
					mark += 1;
					for (int nextindex : G.adj(currentIndex)) {
		                if (!vmarked[nextindex]) {
		                    vedgeTo[nextindex] = currentIndex;
		                    vdistTo[nextindex] = vdistTo[currentIndex] + 1;
		                    vmarked[nextindex] = true;
		                    vQueue.enqueue(nextindex);
		                    if (wmarked[nextindex] == true)
		                    	if ((vdistTo[nextindex] + wdistTo[nextindex]) < minLength)
		                    	{
		                    		ancestor = nextindex;
		                    		minLength = vdistTo[nextindex] + wdistTo[nextindex];
		                    	}	                    			                    		
		                }
		            }
				}          
			}
			
			if (!wQueue.isEmpty())
			{
				int currentIndex = wQueue.dequeue();
				if (wdistTo[currentIndex] < minLength)
				{
					mark += 1;
					for (int nextindex : G.adj(currentIndex)) {
		                if (!wmarked[nextindex]) {
		                    wedgeTo[nextindex] = currentIndex;
		                    wdistTo[nextindex] = wdistTo[currentIndex] + 1;
		                    wmarked[nextindex] = true;
		                    wQueue.enqueue(nextindex);
		                    if (vmarked[nextindex] == true)
		                    	if ((vdistTo[nextindex] + wdistTo[nextindex]) < minLength)
		                    	{
		                    		ancestor = nextindex;
		                    		minLength = vdistTo[nextindex] + wdistTo[nextindex];
		                    	}	                    			                    		
		                }
		            }
				}          
			}
			
			if (mark == 0)
				break;
		}
		return ancestor;
	}
	
	public static void main(String[] args) {
		In in = new In(args[0]);
	    Digraph G = new Digraph(in);
	    SAP sap = new SAP(G);
	    while (!StdIn.isEmpty()) {
	        int v = StdIn.readInt();
	        int w = StdIn.readInt();
	        int length   = sap.length(v, w);
	        int ancestor = sap.ancestor(v, w);
	        StdOut.printf("length = %d, ancestor = %d\n", length, ancestor);
	    }
	}
}


