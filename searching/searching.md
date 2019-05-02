<a href="home.html">Main Page</a>  
Previous: <a href="bst_overview.html">Overview of Balance and Efficiency</a>

## Searching Search Trees

Given any search tree, the algorithm to find and access an element is essentially the same.  

Given a search key, starting with the root:

		If search key < root value  
			Search left subtree  
		Elseif search key > root value  
			Search right subtree  
		Elseif search key == root value  
			return root

Some trees have more than one value in each node. B-Trees can contain multiple data items in a node and can also link to four children.  

Searching these trees is still quite easy.

		If search key < first root value  
			Search left subtree  
		Elseif search key == first root value  
			Return first root value  
		Elseif search key < second value  
			Search second left subtree  
		Elseif search key == second root value  
			Return second root value  
			.  
			.  
			.  
		Elseif search key == last root value  
			Return last root value  
		Elseif search key > last root value  
			Search right subtree  


This algorithm is a combination of:  
-sequential search (searching through data itmes for each node)  
-binary search (searching smaller or larger subarray based on root value)  

Back to <a href="home.html">Main Page</a>  




<style type="text/css" rel="stylesheet">

img[src~="th"] {
   width:150px;
}
img[src~="thl"] {
	width:225px;
}
img[src~="bordered"] {
   border: 1px solid black;
}
img[src~="md"] {
   width:350px;
}
img[src~="mdl"] {
	width:500px;
}
img[src~="large"] {
   width:700px;
}
</style>