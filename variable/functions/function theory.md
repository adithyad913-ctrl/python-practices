#### **Function in Python**

**=====================================================================================**



A function is a **reusable block** of code that performs a **specific task**. 

Instead of writing the same code again and again, we create a function once and call it whenever we need that task.



**Advantages of Functions:**



1. Reuse code multiple times.
2. Reduce code repetition.
3. Improve readability.
4. Make debugging easier.
5. Simplify maintenance.
6. Organize programs into smaller modules.
7. Make testing easier.
8. Support teamwork.
9. Reduce development time.
10. Simplify complex programs.



**Limitations of Functions:**



1. Slightly increases execution time.
2. Uses additional memory.
3. Too many functions can make the code difficult to understand.
4. Requires proper naming and organization.
5. Debugging can be more difficult when many functions are interconnected.

===================================

**Types of Functions in Python**



Python provides two types of functions:



1. Built-in Functions
2. User-defined Functions



**1. Built-in Functions**



Built-in functions are **pre-defined functions** that are already available in Python. 

We do not need to create them. We can use them directly whenever needed.



Examples : print(),len(),type(),min(),input()



**2. User-defined Functions**



A user-defined function is a function created by the programmer to perform a specific task.



| Syntax:

| def fun\_name():

| 	# Function body

| 	statements

| fun\_name()



def        → Keyword used to define a function.

fun\_name   → Name of the function.

:          → Indicates the start of the function body.

fun\_name() → Function calling



**Rules for creating a function name in Python:**

**========================================================================**



1\.  function name must start with a letter (A-Z or a-z) or an underscore (\_).



2\.  The function name cannot start with a number.



3\.  The function name can contain:



&#x20;   -   Letters (A-Z, a-z)

&#x20;   -   Numbers (0-9)

&#x20;   -   Underscores (\_)



4\.  Special characters are not allowed.



&#x20;   -   Examples: @, #, $, %, -, space, etc.



5\.  Do not use Python keywords as function names.



&#x20;   -   Examples: if, for, while, class, def, return



6\.  Function names are case-sensitive.



&#x20;   -   add() and Add() are treated as two different functions.



7\.  Use meaningful and descriptive names.



&#x20;   -   Good: calculate\_area(), find\_maximum()

&#x20;   -   Bad: abc(), fun1()



8\.  Use lowercase letters for function names.



&#x20;   -   This follows the Python naming convention.



9\.  Use underscores (\_) to separate multiple words.



&#x20;   -   Example: student\_details(), calculate\_salary()



**====================================================================================================**

&#x20;        **HOW A FUNCTION WORKS IN PYTHON**

**====================================================================================================**



**Step 1:** Write (Define) the Function , Use the 'def' keyword to create a function.



Syntax:

def function\_name():

&#x20;   statements



Example:

def greet():

&#x20;   print("Welcome")



greet()



\--------------------------------------------------



**Step 2:** Call the Function

&#x20;       ↓

Use the function name followed by ().



Syntax:

function\_name()



Example:

greet()



\--------------------------------------------------



**Step 3:** Function Executes

&#x20;       ↓

Python goes to the function,

executes the statements,

displays the output,

and returns to the next line of the program.



======================================================================================================

**Practice questions**

=======================================================================================================

1. Print Your Name
2. Print Numbers from 1 to 5

========================================================================================================

&#x20;         **PARAMETERS AND ARGUMENTS IN PYTHON**

========================================================================================================



**1. What is a Parameter?**



A parameter is a **variable** written inside the parentheses when defining a function.

It acts as a placeholder to receive a value.



| Syntax:

| def function\_name(parameter):

|    statements



Example:

def greet(name):

&#x20;   print("Hello", name)



**'name' is the parameter.**



\----------------------------------------------------------



**2. What is an Argument?**



An argument is the actual value passed to the function when it is called.



| Syntax:

| function\_name(argument)



Example:

greet("John")



"John" is the argument.



\----------------------------------------------------------



3\. Complete Example



def greet(name):

&#x20;   print("Hello", name) 



greet("John") 



Output:

Hello John



Parameter : name

Argument  : John



==================================================

&#x20;       FUNCTION EXECUTION FLOW

==================================================



Step 1

Python reads the program

&#x20;       │

&#x20;       ▼



Step 2

Finds the function



def greet(name):

&#x20;   print("Hello", name)



✔ Function is created.

✔ Stored in memory.

✘ Not executed.

it executes only after the function call.



&#x20;       │

&#x20;       ▼



Step 3

Python continues reading



greet("John")



&#x20;       │

&#x20;       ▲

&#x20;       │

(Jumps to the function)



Step 4

name = "John"



&#x20;       │

&#x20;       ▼



Step 5

print("Hello", name)



&#x20;       │

&#x20;       ▼



Output:

Hello John



&#x20;       │

&#x20;       ▼



Step 6

Function ends and returns

to the next line.

\----------------------------------------------------------



**4. Difference Between Parameter and Argument**



**Parameter**

\- Written in the function definition.

\- It is a variable.

\- Receives the value.



**Argument**

\- Passed during the function call.

\- It is the actual value.

\- Sends the value to the parameter.



\---------------------------------------------------------



Parameter:

A variable that receives a value in a function definition.



Argument:

The actual value passed to a function when it is called.

**==========================================================**

&#x20;         **TYPES OF USER-DEFINED FUNCTIONS**

**==========================================================**

1\. Function without Arguments

&#x20;  (No input, No return value)



2\. Function with Arguments

&#x20;  (Input, No return value)



3\. Function without Arguments with Return Value

&#x20;  (No input, Returns a value)



4\. Function with Arguments with Return Value

&#x20;  (Input, Returns a value)



==========================================================

&#x20;            **1. FUNCTION WITHOUT ARGUMENTS**

==========================================================



Definition:

A function without arguments is a function that does not accept any input (arguments) when it is called.

It performs a predefined task without requiring any input.



Syntax:



def function\_name():

&#x20;   statements



function\_name()



\----------------------------------------------------------

Example:



def greet():

&#x20;   print("Hello")



greet()          # Function Call



Output:

Hello



==========================================================

&#x20;             **2. FUNCTION WITH ARGUMENTS**

==========================================================



Definition:

A function with arguments is a function that accepts one or

more values (arguments) when it is called. These values are

received by the function through parameters.



Syntax:



def function\_name(parameter):

&#x20;   statements



function\_name(argument)



\----------------------------------------------------------

Example:



def greet(name):

&#x20;   print("Hello", name)



greet("John")      # Function Call



Output:

Hello John

**----------------------------------------------------------**

**3. Function without Arguments with Return Value**

**----------------------------------------------------------**



Definition:

A function that does not take any arguments (input) but

returns a value using the 'return' keyword.



return:

The 'return' keyword is used to send a value from a function

back to the place where it was called.



Syntax:



def function\_name():

&#x20;   return value



result = function\_name()

print(result)



\----------------------------------------------------------

Example



def add():

&#x20;   return 10 + 20



result = add()

print(result)



Output:

30



\----------------------------------------------------------

Explanation



\- The function takes no arguments.

\- The function is called using add().

\- The 'return' statement sends the value 30 back.

\- The returned value is stored in the variable 'result'.

\- print(result) displays the output.



\----------------------------------------------------------

Execution Flow



Python reads:



def add():

&#x20;   return 10 + 20



✔ Function is created.

✘ Not executed yet.



&#x20;       │

&#x20;       ▼



result = add()



✔ Function is called.



&#x20;       │

&#x20;       ▲

&#x20;       │

Python enters the function.



return 10 + 20



&#x20;       │

&#x20;       ▼



Returns 30



&#x20;       │

&#x20;       ▼



The returned value is stored in 'result'.



&#x20;       │

&#x20;       ▼



result = 30



&#x20;       │

&#x20;       ▼



print(result)



&#x20;       │

&#x20;       ▼



Output:

30

**----------------------------------------------------------**

**4. Function with Arguments with Return Value**

**----------------------------------------------------------**



Definition:

A function that takes input through arguments and returns

a value using the 'return' keyword.



Syntax:



def function\_name(parameters):

&#x20;   return value



result = function\_name(arguments)

print(result)



\----------------------------------------------------------

Example



def add(a, b):

&#x20;   return a + b



result = add(10, 20)

print(result)



Output:

30



\----------------------------------------------------------

Explanation



\- The function takes two arguments (10 and 20).

\- The arguments are stored in the parameters (a and b).

\- The function adds the values.

\- The 'return' statement sends the result back.

\- The returned value is stored in 'result'.

\- print(result) displays the output.



\----------------------------------------------------------

Execution Flow



Python reads:



def add(a, b):

&#x20;   return a + b



✔ Function is created.

✘ Not executed yet.



&#x20;       │

&#x20;       ▼



result = add(10, 20)



✔ Function is called.



&#x20;       │

&#x20;       ▲

&#x20;       │

Python jumps to:



a = 10

b = 20



&#x20;       │

&#x20;       ▼



return a + b



&#x20;       │

&#x20;       ▼



Returns 30



&#x20;       │

&#x20;       ▼



result = 30



&#x20;       │

&#x20;       ▼



print(result)



&#x20;       │

&#x20;       ▼



Output: 30



==========================================================

&#x20;        DIFFERENT WAYS TO PASS ARGUMENTS

==========================================================



Python provides four ways to pass arguments to a function.



1\. Positional Arguments

2\. Keyword Arguments

3\. Default Arguments

4\. Variable-Length Arguments (\*args)



\----------------------------------------------------------

1\. Positional Arguments

\----------------------------------------------------------



Definition:

Arguments are passed in the same order as the parameters.



Example:



def student(name, age):

&#x20;   print(name, age)



student("John", 20)



Output:

John 20



\----------------------------------------------------------

2\. Keyword Arguments

\----------------------------------------------------------



Definition:

Arguments are passed using the parameter names.

The order of arguments does not matter.



Example:



def student(name, age):

&#x20;   print(name, age)



student(age=20, name="John")



Output:

John 20



\----------------------------------------------------------

3\. Default Arguments

\----------------------------------------------------------



Definition:

A parameter is given a default value. If no argument is

passed, the default value is used.



Example:



def greet(name="John"):

&#x20;   print("Hello", name)



greet()



Output:

Hello John



\----------------------------------------------------------

4\. Variable-Length Arguments (\*args)

\----------------------------------------------------------



Definition:

Allows a function to accept any number of arguments.



Example:



def add(\*numbers):

&#x20;   print(sum(numbers))



add(10, 20, 30, 40)



Output:

100



==========================================================

&#x20;               VARIABLE SCOPE IN PYTHON

==========================================================



Definition:

Variable scope refers to the area of a program where a

variable can be accessed or used.



Python has two types of variable scope:



1\. Local Variable

2\. Global Variable



==========================================================

1\. LOCAL VARIABLE

==========================================================



Definition:

A local variable is created inside a function and can be

used only within that function.



Syntax:



def function\_name():

&#x20;   variable = value



Example:



def greet():

&#x20;   name = "John"

&#x20;   print(name)



greet()



Output:

John



Explanation:

\- 'name' is a local variable.

\- It can be accessed only inside greet().

\- It cannot be used outside the function.



==========================================================

2\. GLOBAL VARIABLE

==========================================================



Definition:

A global variable is created outside a function and can be

used both inside and outside the function.



Syntax:



variable = value



def function\_name():

&#x20;   statements



Example:



name = "John"



def greet():

&#x20;   print(name)



greet()

print(name)



Output:

John

John



Explanation:

\- 'name' is a global variable.

\- It can be accessed inside the function.

\- It can also be accessed outside the function.



==========================================================

DIFFERENCE BETWEEN LOCAL AND GLOBAL VARIABLE

==========================================================



Local Variable

\- Declared inside a function.

\- Accessible only inside the function.

\- Exists only during function execution.



Global Variable

\- Declared outside a function.

\- Accessible throughout the program.

\- Exists until the program ends.



==========================================================



