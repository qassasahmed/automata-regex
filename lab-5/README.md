# Lab (5) Notes
Ahmed Al-Qassas  
[qassas.ahmed@mau.edu.eg](qassas.ahmed@mau.edu.eg)  
---


# 0 Python's re module

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







