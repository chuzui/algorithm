
public class Outcast {

	private WordNet _wordNet;
	
	// constructor takes a WordNet object
	public Outcast(WordNet wordnet)
	{
		_wordNet = wordnet;
	}

	// given an array of WordNet nouns, return an outcast
	public String outcast(String[] nouns)
	{
		int maxDistance = 0;
		String outcast = null;
		for (String iString : nouns)
		{
			int distance = 0;
			for (String jString : nouns)
			{
				distance += _wordNet.distance(iString, jString);
			}
			if (distance >= maxDistance)
			{
				maxDistance = distance;
				outcast = iString;
			}
		}
		
		return outcast;
	}

	// for unit testing of this class (such as the one below)
	@SuppressWarnings("deprecation")
	public static void main(String[] args)
	{
		WordNet wordnet = new WordNet(args[0], args[1]);
	    Outcast outcast = new Outcast(wordnet);
	    for (int t = 2; t < args.length; t++) {
	        String[] nouns = In.readStrings(args[t]);
	        StdOut.println(args[t] + ": " + outcast.outcast(nouns));
	    }
	}
}
