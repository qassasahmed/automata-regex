# Lab (5) Notes
Ahmed Al-Qassas  
[qassas.ahmed@mau.edu.eg](qassas.ahmed@mau.edu.eg)   

---


# 1 Python's re module

* Most letters and characters will simply match themselves.
* Metacharacters do not match themselves.
* Special sequences beginning with '\'.

## Example 1: 
Using re module, write a python function that matches a string that has an a followed by three 'b'
```python
def check_string5(string): 
    pattern = re.compile(r'^ab{3}$')
    return 'valid' if pattern.match(string) else 'invalid'
```
* The pattern itself is defined within `r''` **(raw string notation)** to avoid escaping special characters within the string.
* `^`: Matches the beginning of the string.
* `a`: Matches the character "a" exactly once.
* `b`: Matches the character "b" exactly once.
* `{3}`: Quantifier that matches the preceding character ("b" in this case) exactly 3 times.
* `$`: Matches the end of the string.
## Example 2:
Using re module, write a python function that matches a string that has an a followed by \[2:4\] 'b'. The letters can be lowercase or uppercase.
```python
def check_string6(string):
    pattern = re.compile(r'^ab{2,4}$', re.I)
    return 'valid' if pattern.match(string) else 'invalid'
```
* `re.I` or `re.IGNORECASE` a [flag](https://docs.python.org/3/library/re.html#flags "read more about re flags") that ctivates case-insensitive matching.
* `{2,4}`: Matches the preceding character ("b" in this case) \[2:4\]  characters (case-insensitive).
## Example 3: 
Using re module, write a python function to find sequences of lowercase letters joined with an underscore `_`.

```python
def check_string7(string):
    pattern = re.compile(r'^[a-z]+_[a-z]+$')
    return pattern.match(string)
    # <re.Match object; span=(0, 11), match='blueh_blueh'>
```
* `[a-z]+`: Matches one or more lowercase letters (a to z). The `+` quantifier ensures there's at least one lowercase letter.

## [More Examples 1-9](rexamples.py)

## Match Objects 
The re module provides some functions to help developers use the regular expression.
Most of these function return a match object.  
For example, ` <re.Match object; span=(0, 11), match='blueh_blueh'> `from the previous example is a match object. the `span` argument refers to the start and end where the object exists and the `match` argument refers to the match string itsef.

Other functions that are provided through re are:
1. re.search
2. re.match
3. re.fullmatch
4. re.finditer
5. re.findall
6. re.split
7. re.sub or re.subn

We have discussed the `re.fullmatch` previously. It requires the whole string to match the compiled re pattern. Both `re.search` and `re.match` do not require the whole string to match the pattern, a subset is enough. But what are the differences between `re.search` and `re.match`? **Try to answer it yourself and provide an example.**

---

# 2 Context Free Grammar CGF
**CFGs are more expressive than Finite Automata** , meaning they can describe a broader set of languages, including those that have nested structures or dependencies that cannot be captured by Finite Automata.

Finite Automata are often used for tasks like lexical analysis in compilers, where patterns can be described using regular expressions and recognized efficiently using automata.  

Context-Free Grammars are more suited for tasks like syntactic analysis in compilers, where the hierarchical structure of the language needs to be analyzed.

## CGF Repersentation
Context-Free Grammars are often represented as a 4-tuple: **(V, Σ, R, S)**  
In every production of a CFG, at the left hand side there is a single non-terminal.

## Example (6.3)
Construct a CFG for `L = (011 + 1)*(01)*`   
S → BC  
B → AB | ε  
A → 011 | 1   
C → DC | ε  
D → 01   
Where 
`V`: {S, A, B, C, D}  
`Σ` : {0, 1}  
`S` : {S}
  
**What about this production rule?**  
S → AB  
A → 011A | 01A | ε  
B → 01B | ε  

## Problem (1)  
**page #346**: Construct a CFG for set of string of 0 and 1 where consecutive 0 can occur but no consecutive 1 can occur.  
We start at S. From S we can have 0 or 1, form 0 we can have 0 or 1, from 1 we can have only 0.  

S → 0S  
S → 1A  
S → 0    
S → 1     
A → 0S    
A → 0   

## Problem (4)
**page #348**: Let G be the grammar `S → aB/ba, A → a/aS/bAA, B → b/bS/aBB`. For the string **aaabbabbba** ﬁnd a
### 1. Leftmost derivation  
A derivation is called a leftmost derivation if we **replace only the leftmost
non-terminal** by some production rule at each step of the generating process of the language from the grammar.  

S → a**B** → aa**B**B → aaa**B**B → aaab**B**B → aaabb**S**B → aaabba**B**B → aaabbab**B** → aaabbabb**S** → aaabbabbba  
### 2. Rightmost derivation  
Here we repalce only the rightmost non-terminal.  

S → a**B** → aaB**B** → aaBb**S** → aa**B**bba → aaaB**B**bba → aaa**B**bbba → aaab**S**bbba
→ aaabbabbba  
### 3. Parse tree    
![](figs/tree.png)  
![](figs/parse-tree-p4.png)  

# 3 Concolusion

## The Chomsky Hierarchy
It is hierarchy of formal languages based on the properties of the grammars
required to generate the languages. Chomsky classified the grammar into **four** types depending on the _production_ rule:  

| Grammar  | Language                   | Machine Format          |
|:---------|:---------------------------|:------------------------|
| _Type 0_ | Unrestricted Language      | Turing Machine          |
| _Type 1_ | Context-sensitive language | Linear bounded automata |
| _Type 2_ | Context-free language      | Push down automata      |
| _Type 3_ | Regular Expression         | Finite automata (FSM)   |

According to the Chomsky hierarchy, we know that a regular grammar is a subset of CFG. Thus, for
every regular language, there exists a CFG. In this section, we shall discuss two theorems related to this
**Theorem 1**: Every regular language is generated by a CFG.
















