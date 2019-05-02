<a href="home.html">Main Page</a>  
<a href="sequential.html">Sequential Search</a>  
Back: <a href="binary_search.html">Binary Search</a>

# Indexed Sequential Search

### Background
- a.k.a. ISAM - Indexed Sequential Access Method, developed by IBM
- requires sorted data
- uses an auxiliary table to hold indices and pointers to a subset of actual records
- size of index table depends on application
- can have multiple levels of index tables

![Indexed Sequential Search](media/ind1.png# md)

### Algorithm

	Perform sequential search on outermost index table
	If record is found, return it.
	If index is greater than search key, perform sequential search on lower nested index table or actual records starting from previous index in index table


### Efficiency

Time complexity is reduced compared to sequential search but not as efficient as binary search.  
The complexity is wholly dependent on the design of the index table. Efficiency is somewhere between O(log n) and O(n), however in order to approach an efficiency of O(log n), the data will start to approach the form of a balanced binary search tree.

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