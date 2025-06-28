## makeCacheMatrix is a function that takes in a matrix as an
## argument and gives out a list of functions that get or set this value
## and also get or set the inverse of the matrix given as an argument originally

makeCacheMatrix <- function(x=matrix()) {
	inv <- NULL
	set <- function(s) {
		x <<- s
		inv <<- NULL}

	get <- function() x

	set_inv <- function(i) {
		inv <<- solve(x)}

	get_inv <- function() inv

methods = list(set=set,get=get,set_inv=set_inv,get_inv=get_inv)
}


## cacheSolve is a function that takes in 'the output of "makeCacheMatrix"
## as an argument and gives out the inverse of the matrix (that is already
## stored in the makeCacheMatrix object) OR calculates the inverse in case
## a new matrix has replaced the older one in the makeCacheMatrix object.

cacheSolve <- function(b,...) {
	inv_check <- b$get_inv()

	if(!is.null(inv_check)) {
		message("Getting Cached Data")
		return(inv_check)}
	
	matrx <- b$get()
	inv_check <- solve(matrx, ...)
	b$set_inv(inv_check)
inv_check
}
