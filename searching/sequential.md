<a href="home.html">Main Page</a>

# Sequential Search

### Background
- does not require sorted data
- used with array, linked list such as:

![Sequential Search Table](media/seq1.png# md)

- cannot leave holes in array
	- deletion requires shifting records

### Algorithm

Sequentially search a table for a given key:

	For each record, compare if it is the given key.
	If not, keep looking,
	If it is, return the key.

### Efficiency

On average, sequential search will take (n+1)/2 comparisons. There are some subtleties, depending on whether the key sought is unique or may be duplicated, as well as between sorted and unsorted data.  
On average, sequential sort will be O(n).

For more details, review your Homework 9, Question 1: <a href="sequential_efficiency.html">Sequential Sort Efficiency</a>


Next: <a href="binary_search.html">Binary Search</a>  
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