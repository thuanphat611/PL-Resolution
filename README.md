### Problem description
![PL-Resolution algorithm.](/Document/pl_resolution.png)
Implement the PL-RESOLUTION function to determine if a given
knowledge base (KB) entails a query α. Both the KB and α are sets of propositional clauses
in CNF. 
### Specifications
**Input:** The file contains the knowledge base (KB) and query α in the following format:
- First line contains a positive integer M, which is the number of clauses in query α.
- M next lines represent the clauses in query α, one clause per line.
- M + 2 line contains a positive integer N, which is the number of clauses in the KB.
- N next lines represent the clauses in KB, one clause per line.

A positive literal is denoted by an uppercase letter (A-Z), while a negated literal is denoted
by a minus symbol (‘-’) preceding the literal. Literals are connected using the OR keyword.
There may be multiple whitespace characters between literals and keywords.\
**Output:** The file contains the generated clauses and the conclusion in the following format:
- The first line indicates the number of clauses generated in the first loop (M1).
- The subsequent M1 lines represent the newly generated clauses in the first loop,
including the empty clause represented as "{}".
- Subsequent loops (M2, ..., Mn clauses) follow the same format as mentioned above.
- The last line displays the conclusion, indicating whether the KB entails α. Print
"YES" if the KB entails α; otherwise, print "NO".
- Duplicate clauses, meaning clauses that are identical to previously appeared clauses
(in the current/previous loop or in the original KB), are disregarded.

**Notes:** 
- The literals within each clause, both in the input data and output data, should be
sorted in alphabetical order.
- The entailment check is performed at the end of each loop, rather than after
generating a clause.
- The clause (A V B V −B) is considered equivalent to (A V True) and thus equivalent
to True. Deriving that True is true does not provide useful information. Therefore,
any clause that contains two complementary literals can be disregarded.
- It is assumed that the input data is in a valid format.
###  Example 
Here is an example of the provided KB and query α in the input.txt file.
![Example input.txt and output.txt.](/Document/example.png)
