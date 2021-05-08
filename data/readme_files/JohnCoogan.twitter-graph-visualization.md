Twitter Graph Visualization
===========================

The goal of this project is to apply some of the machine learning concepts I've learned so far to my own personal data. Code in this repo contains everything needed to perform the same analysis on yourself. Everything from collecting and cleaning the data, to running the analyses, to finally visualizing output is here.

Files
-----
*	**twitter.py:** Scrape and clean twitter data.
*	**analysis.py:** Read in Edge List and generate analysis and graph data.
*	**community.py:** A community detection module for NetworkX.
*	**server.py:** A Flask App to host the visualization.
*	**oauth.json:** Contains personal config vars in a dictionary (not checked in)

OAuth.json
----------

	{
		"consumer_key" : "key",
		"consumer_secret" : "secret",
		"access_token" : "key",
		"access_token_secret" : "secret",
		"screen_name" : "name",
		"user_id" : 12345678
	}

Discussion:
-----------
Here's what's going on so far:

### Intro
Visualizion network graphs is pretty tough still, but NetworkX and D3.js take a lot of the hassle out of it.

*	Collect data from Twitter
*	Read in the edgelist to NetworkX
*	Convert it to a Network X graph object
*	Calculate statistics & save values as nodes
*	Write out JSON of nodes, edges and their attributes
*	Visualize using D3.js

### Data Collection
First, we have to scrape our first and second order networks on twitter to construct an edgelist. This gives us information for everyone the selected user follows as well as all the people that are followed by the users they follow. Once we have an edge list, we can start working with Network X.

### Analysis
The statistics I focused on are as follows:
*	**Degree Centrality** focuses on individual nodes, counting the number of edges a node has. Nodes with high degree usually play an important role in a network. The degree centrality for a node is the fraction of nodes it is connected to.
	*	The degree centrality values are normalized by dividing by the maximum possible degree in a simple graph n-1 where n is the number of nodes in G.

*	**Eigenvector Centrality** measures the importance of a node proportional to the sum of the centrality scores of its neighbors. In other words, a node is important if it is connected to other important nodes.
	*	Calculate the eigendecomposition of the pairwise agjacency matrix of the graph.
	*	Select the eigenvector associated with the largest eigenvalue.
	*	Element *i* in the eigenvector gives the centrality of the i-th node.
	*	**Note:** The eigenvector calculation is done by the power iteration method and has no guarantee of convergence.

*	**Louvain Method** of community detection. The method is a greedy optimization method that attempts to optimize the "modularity" of a partition of the network. The optimization is performed in two steps. 
	*	First, the method looks for "small" communities by optimizing modularity locally. 
	*	Second, it aggregates nodes belonging to the same community and builds a new network whose nodes are the communities. 
	*	These steps are repeated iteratively until a maximum of modularity is attained and a hierarchy of communities is produced. 
	*	**Note:** Although the exact computational complexity of the method is not known, the method seems to run in time O(n log n) with most of the computational effort spent on the optimization at the first level. Exact modularity optimization is known to be NP-hard.

### Visualization
I chose to use a force-directed graph because I think it strikes a nice balance between showing a lot statistics simultaneously while still being fairly simple to understand.
*	The implementation I chose uses a quadtree to accelerate charge interaction using the Barnes–Hut approximation.
*	The graph optimizes the position of the nodes in two-dimensional space such that all the edges are close to equal length and there are as few crossing edges as possible.
*	To further emphasize the centrality values, I set the size of each node proportional to the selected centrality value (either eigenvector or degree).
*	I added color to each node to show the communities that the Louvain method detected.


TODO:
-----
*	Add description of what's going on to front-end
*	Work on Twitter rate limiting issues.
*	Create modular version with Twitter OAuth. (Look at rate-limits first)
