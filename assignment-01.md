

# CMPS 2200 Assignment 1

**Name:** Zachary Hom


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes, because there exists some c > 2 such that 2^{n+1} < c*2^n.
lim as x --> infinity of [2^{n+1}/2^n] == 2.
.  
.
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No, because there does not exist some c such that 2^{2^n} < c*2^n.
lim as x --> infinity of [2^{2^n}/2^n] --> infinity.
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
. No, because there does not exist some c such that n^{1.01} < c*\mathrm{log}^2 n for large values of n.
lim as x --> infinity of [n^{1.01}/mathrm{log}^2 n] --> infinity.
.  
.  
.  
  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes, because lim as n --> infinity of [n^{1.01}/mathrm{log}^2 n] --> infinity which means that mathrm{log}^2 n bounds n^{1.01} from below.
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No, because there does not exist some value c such that sqrt{n} < c*mathrm{log} n)^3) for large values of n.
lim as x --> infinity of [sqrt{n}/mathrm{log} n)^3] --> infinity.
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?
.  Yes, because lim as x --> infinity of [sqrt{n}/mathrm{log} n)^3] --> infinity which means mathrm{log} n)^3 bounds sqrt{n} from below


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  
  DONE.

  - 2b. (6 pts) What does this function do, in your own words?  
This function takes in an input and recursively calls itself with inputs x-1 and x-2 added together; therefore, it returns the x'th number in the Fibonacci sequence of numbers. 
.  
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.
  DONE.

  - 3b. (4 pts) What is the Work and Span of this implementation?  
Work: O(n) -- must run through each element of the input one at a time so runtime is O(n)
Span: O(n) -- sequential, cannot run multiple iterations at the same time even with more processors
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
  ** Dr. Ding said this means the recursive function on ONE processor (no parallelization possible) **
Work: O(n)
Span: O(n) -- because parallelization is not possible in this scenario, span would still be O(n) because multiple threads created by recursion could not be run at the same time
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
Work: O(n)
Span: O(log2_n) -- because parallelization is possible in this scenario, span would be O(log2_n) because multiple threads created by recursion can be run at the same time
.  
.  
.  
.  
.  
.  
.  
.  

