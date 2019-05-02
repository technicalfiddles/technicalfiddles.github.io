<a href="home.html">Main Page</a>  
Previous: <a href="sequential.html">Sequential Search</a>

# Binary Search

### Background
- requires sorted data
- most efficient method that doesn't store auxiliary indices (the ways trees do)

### Algorithm

	Compare middle element of table with given key. 
	If equal, return element.
	If middle element less than key, search first half of table
	Else search second half of table


### Efficiency

Due to the searchable space being halved after each comparison, this is a log(n) operation. Thus the efficiency on average is O(log n).

Next: <a href="indexed_sequential.html">Indexed Sequential Search</a>  
<a href="home.html">Main Page</a>

