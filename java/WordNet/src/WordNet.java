import java.util.ArrayList;

public class WordNet {

	private ST<String, Bag<Integer>> st;
	//private ArrayList<String> keys;
	private ArrayList<String> setkeys;
	private Digraph G;
	private SAP sap;
	//constructor takes the names of the two input files
	public WordNet(final String synsets, final String hypernyms)
	{
		//Graph undirectedGraph;
		st = new ST<String, Bag<Integer>>();
		//keys = new ArrayList<String>();
		setkeys = new ArrayList<String>();
		int graphSize = 0;
		try {
			In synsetsIn = new In(synsets);
			In hypernymsIn = new In(hypernyms);

			while (synsetsIn.hasNextLine())
			{
				String[] infoStrings = synsetsIn.readLine().split(",");
				int index = Integer.parseInt(infoStrings[0]);
				
				try
				{
					String[] sysnetsStrings = infoStrings[1].split(" ");
					for (String word : sysnetsStrings)
					{		
						if (!st.contains(word))
						{
							st.put(word, new Bag<Integer>());
						}
						st.get(word).add(index);
						//keys.add(word);
					}
					graphSize += 1;
					setkeys.add(index, infoStrings[1]);					
				}
				catch (Exception e)
				{			
					
				}
			}

			G = new Digraph(graphSize);
			//undirectedGraph = new Graph(keys.size());
			while (hypernymsIn.hasNextLine())
			{
				String[] infoStrings = hypernymsIn.readLine().split(",");
				
				try {
					for (int i = 1; i < infoStrings.length; i++)
					{
						G.addEdge(Integer.parseInt(infoStrings[0]), 
								Integer.parseInt(infoStrings[i]));
						//undirectedGraph.addEdge(Integer.parseInt(infoStrings[0]),
						//		Integer.parseInt(infoStrings[i]));
					}
				} catch (Exception e) {
				}
			}
			
		} catch (Exception e) {
			throw new IllegalArgumentException();
		}
		
		boolean isRootDAG = true;
		
		//CC cc = new CC(undirectedGraph);
		//if (cc.count() > 1)
		//	isRootDAG = false;
		
		DirectedCycle cycle = new DirectedCycle(G);
		if (cycle.hasCycle())
			isRootDAG = false;
		
		int rootCount = 0;
		for (int i = 0; i < G.V(); i++)
		{
			if (!G.adj(i).iterator().hasNext())
				rootCount += 1;			
		}
		if (rootCount != 1)
			isRootDAG = false;
		
		if (isRootDAG == false)
			throw new IllegalArgumentException();
		
		sap = new SAP(G);	
	}
	
	public Iterable<String> nouns()
	{
		return st.keys();
	}
	
	public boolean isNoun(final String word)
	{
		return st.contains(word);
	}
	
	public int distance(final String nounA, final String nounB)
	{
		if (!isNoun(nounA) || !isNoun(nounB))
			throw new IllegalArgumentException();
		return sap.length(st.get(nounA), st.get(nounB));
	}
	
	public String sap(final String nounA, final String nounB)
	{
		if (!isNoun(nounA) || !isNoun(nounB))
			throw new IllegalArgumentException();
		return setkeys.get(sap.ancestor(st.get(nounA), st.get(nounB)));
	}
	
	public static void main(final String[] args)
	{
		WordNet neWordNet = new WordNet("wordnet/synsets.txt", "wordnet/hypernyms.txt");
		while (!StdIn.isEmpty()) {
	        String v = StdIn.readString();
	        String w = StdIn.readString();
	        int length   = neWordNet.distance(v, w);
	        String ancestor = neWordNet.sap(v, w);
	        StdOut.printf("length = %d, ancestor = %s\n", length, ancestor);
	    }
	}
}
