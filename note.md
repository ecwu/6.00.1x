# Introduction to Computer Science and programming using python

> edX MITx 6.00.1x SUMMER 2017

[TOC]

----

## Python Basics

### Knowledge

* declarative knowledge: Statements of fact
* imperative knowledge: recipe (**More value**)

### Machines

#### Fixed program computer (Finish specific task)

* Calculator
* Alan Turing‘s Bombe

#### Stored Program Computer 

Machine stores and executes instructions.

* Sequence of instructions stored inside computer built from predefined set of primitive instructions
  * arithmetic and logic
  * simple tests
  * moving data
* special program(interpreter) execute each instruction in order
  * use tests to change flow of control through sequence
  * stop when done

##### Basic Machine architecture:

![Image result for Basic Machine architecture](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Von_Neumann_architecture.svg/2000px-Von_Neumann_architecture.svg.png)

#### Basic Primitives

Turing Machine: compute anything with six primitives.

move left, move right, scan, print, write, do nothing.

**abstract methods to create new primitives**



> Q: What does it mean when we say that "the computer walks through the sequence executing some computation"?
>
> A: **The computer executes the instructions mostly in a linear sequence, except sometimes it jumps to a different place in the sequence.** 

### Language

Experience are complex but **legal combinations of primitives** in programming language

primitive constructs of programming language: numbers, strings, simple operators.

#### Syntax

* `"hi"*5` not syntactically valid
* `3.2*5` syntactically valid

##### Static Semantics:

Which syntactically valid strings have meaning.

##### Full Semantics:

The meaning associated with a syntactically correct string of symbols with no static semantic errors

Programming languages: have only one meaning but may not be what programmer intended. (Bugs)

#### Errors

1. Syntactic errors

   Common and easily caught

2. Static semantic errors

   Some languages check it.

   **can cause unpredictable behavior**

3. Different meaning that what programmer intended.

   Program crashes, stop running

   Program runs forever(Dead loop)

   Program give an answer but different than expected

> 1. Determines whether a string is legal
>
>    **Syntax**
>
> 2. Determines whether a string has meaning
>
>    **Static Semantics**
>
> 3. Assigns a meaning to a legal sentence
>
>    **Semantics**

### Type

- Program: Sequence of definitions and commands
- Commands(Statements)


Can be typed directly in a shell or stored in a file that is read into the shell and evaluated

#### Objects

* Programs manipulate data objects
* Object have a type that defined the kinds of things programs can do to them
* Objects are 
  * Scalar (cannot be subdivided)
    * int: integers
    * float: real numbers
    * bool: `True` or `False`
    * NoneType
  * Non-scalar (have internal structure that can be accessed)
* Casting (Float to int)

#### Expressions

`<Object>` `<operator>` `<Object>`

* `i+j`	sum
  * `i-j` difference
  * `i*j`product
  * `i/j`division
  * `i//j`**int** division
  * `i%j`remainder
  * `i**j`power

### Variables

* `name` `=` `Value`


* re-bind

### Operators and Branching

* `i>j`
* `i>=j`
* `i<j`
* `i<=j`
* `i==j`
* `i!=j`

#### Branching Programs

* A test
* A block of code to execute if the test is `True`
* An optional block of code to execute if the test is `False`



