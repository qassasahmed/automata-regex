# Lab (3) Notes
Ahmed Al-Qassas [qassas.ahmed@mau.edu.eg](qassas.ahmed@mau.edu.eg)  
Spring 2023-24
----
# 0 Review on Lab (2)
Chomsky structured a hierarchy of formal languages based on the properties of the grammar required to generate the languages.

| Grammar  | Language                   | Machine Format          |
|:---------|:---------------------------|:------------------------|
| _Type 0_ | Unrestricted Language      | Turing Machine          |
| _Type 1_ | Context-sensitive language | Linear bounded automata |
| _Type 2_ | Context-free language      | Push down automata      |
| _Type 3_ | Regular Expression         | Finite automata (FSM)   |

# 1 Use of Automata
The main usefulness is in **lexical analyser** and syntax error. **But what is lexical analyser**?  
Lexical Analysis is the first phase of the compiler also known as a scanner. It converts the High level input program into a sequence of _Tokens_.
[Read this article](https://www.geeksforgeeks.org/introduction-of-lexical-analysis/) for more information.
Example
```C
int main()
{
  // 2 variables
  int a, b;
  a = 10;
 return 0;
}
```
