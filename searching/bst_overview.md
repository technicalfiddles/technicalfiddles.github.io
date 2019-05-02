<a href="home.html">Main Page</a>  
Previous: <a href="indexed_sequential.html">Indexed Sequential Search</a>  
# Balancing Search Trees
## Balance and Efficiency

A search tree is a lot like an extension of Indexed Sequential Search except that instead of using a few nested index tables to break up a larger array, there is an index table for each pair of records.

Recall the depiction of ISAM (Indexed Sequential Access Method):  

![Indexed Sequential Search](media/ind1.png# md)

Using the ISAM analog, an unbalanced tree is like using a poor choice for the index table.  
A completely unbalanced tree will destroy the efficiencies of any search algorithm.  

<figure>
  <p><img src="media/unbalanced.png"
  	top=0px;
  	left=400px;
    width="350" 
    alt="Unbalanced">
  <figcaption>Unbalanced Search Tree</figcaption>
</figure>

In the unbalanced tree above, the only way to traverse the tree is by accessing each node sequentially.  
Searching in this manner will have the same properties as sequential search, that is (n+1)/2 comparisons and O(n) time complexity.


However, if the tree is balanced such that the height is minimized, significant gains in efficiency can be achieved.
In the tree example below, it only takes 4 comparisons to return the value 54, whereas in a completely unbalanced tree (or sorted array) it would take 8 comparisons.

<figure>
  <p><img src="media/balanced.png"
  	top=0px;
  	left=0px;
    width="350" 
    alt="Balanced">
  <figcaption>Balanced Search Tree</figcaption>
</figure>


Searches range from O(log n) to O(n) depending on how well a tree is balanced.



Next: <a href="searching.html">Searching Search Trees</a>  
<a href="home.html">Main Page</a>  




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