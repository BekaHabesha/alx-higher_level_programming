<H1 align="center", height="1500"> <ins> README.md File </ins> </H1>
<H1 align="center"> <ins>  0x03. Python - Data Structures: Lists, Tuples </ins> </H1>

![Write a simple UNIX command interpreter.]( https://media.licdn.com/dms/image/D4E12AQHF7l_aQcusQQ/article-cover_image-shrink_720_1280/0/1678364981042?e=2147483647&v=beta&t=anVh3u88VwVqK9xIM26BHRzufkrd9iha-7qax7MseX0)

#

* File_name: <ins>**README.md file**</ins>
* Created: <ins>**On November 5, 2023**</ins>
* Author: <ins>***Bereket Dereje Mekonnen***</ins>
* Project: <ins>**0x03. Python - Data Structures: Lists, Tuples**</ins>
* GitHub repository: <ins>**alx-higher_level_programming**</ins>
* Directory: <ins>**0x03-python-data_structures**</ins>
* Project Tasks: <ins>**Mandatory and Advanced**</ins>
* Tasks in number: <ins>**15 Tasks (14Mandatory & 1Advanced)**</ins>
* Mandatory_Tasks: <ins>**From Task 0 to 13**</ins>
* Advanced_Tasks: <ins>**Task 14**</ins>
#

### **PROJECT_TITLE:**
<h2 align="center"> <ins>0x03. Python - Data Structures: Lists, Tuples</ins> </h2>

### **GITHUB_REPOSITORY:**
<h2 align="center"> <ins>alx-higher_level_programming</ins> </h2>

### **DIRECTORY:**
<h2 align="center"> <ins>0x03-python-data_structures</ins> </h2>

![Write a simple UNIX command interpreter.]( https://res.cloudinary.com/practicaldev/image/fetch/s--vsp8TPQo--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eqk9up4gzrgz8f7egozd.png)

<h1 align="center"> <ins> PROJECT TASKS (Mandatory and Advanced)</h1> </ins>

<h1 align="center"> MANDATORY_TASKS (From Task 0 to 5)</h1>

## **No. 0. Print a list of integers**
  * <ins>**0-print_list_integer.py**</ins>
    * <ins>**Write a function that prints all integers of a list.**</ins>
      * Prototype:
        * def print_list_integer(my_list=[]):
      * Format: one integer per line. See example
      * You are not allowed to import any module
      * You can assume that the list only contains integers
      * You are not allowed to cast integers into strings
      * You have to use str.format() to print integers

##

## **No. 1. Secure access to an element in a list**
  * <ins>**1-element_at.py**</ins>
    * <ins>**Write a function that retrieves an element from a list like in C.**</ins>
      * Prototype:
        * def element_at(my_list, idx):
      * If idx is negative,
        * the function should return None
      * If idx is out of range (> of number of element in my_list),
        * the function should return None
      * You are not allowed to import any module
      * You are not allowed to use try/except

##

## **No. 2. Replace element**
  * <ins>**2-replace_in_list.py**</ins>
    * <ins>**Write a function that replaces an element of a list at a specific position (like in C).**</ins>
      * Prototype:
        * def replace_in_list(my_list, idx, element):
      * If idx is negative,
        * the function should not modify anything, and
        * returns the original list
      * If idx is out of range (> of number of element in my_list),
        * the function should not modify anything, and
        * returns the original list
      * You are not allowed to import any module
      * You are not allowed to use try/except

##

## **No. 3. Print a list of integers... in reverse!**
  * <ins>**3-print_reversed_list_integer.py**</ins>
    * <ins>**Write a function that prints all integers of a list, in reverse order.**</ins>
      * Prototype:
        * def print_reversed_list_integer(my_list=[]):
      * Format:
        * one integer per line.
      * You are not allowed to import any module
      * You can assume that the list only contains integers
      * You are not allowed to cast integers into strings
      * You have to use str.format() to print integers

##

## **No. 4. Replace in a copy**
  * <ins>**4-new_in_list.py**</ins>
    * <ins>**Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).**</ins>
      * Prototype:
        * def new_in_list(my_list, idx, element):
      * If idx is negative,
        * the function should return a copy of the original list
      * If idx is out of range (> of number of element in my_list),
        * the function should return a copy of the original list
      * You are not allowed to import any module
      * You are not allowed to use try/except

##

## **No. 5. Can you C me now?**
  * <ins>**5-no_c.py**</ins>
    * <ins>**Write a function that removes all characters c and C from a string.**</ins>
      * Prototype:
        * def no_c(my_string):
      * The function should return the new string
      * You are not allowed to import any module
      * You are not allowed to use str.replace()

##

## **No. 6. Lists of lists = Matrix**
  * <ins>**6-print_matrix_integer.py**</ins>
    * <ins>**Write a function that prints a matrix of integers.**</ins>
      * Prototype:
        * def print_matrix_integer(matrix=[[]]):
      * Format:
        * see example
      * You are not allowed to import any module
      * You can assume that the list only contains integers
      * You are not allowed to cast integers into strings
      * You have to use str.format() to print integers

##

## **No. 7. Tuples addition**
  * <ins>**7-add_tuple.py**</ins>
    * <ins>**Write a function that adds 2 tuples.**</ins>
      * Prototype:
        * def add_tuple(tuple_a=(), tuple_b=()):
      * Returns a tuple with 2 integers:
        * The first element should be the addition of the first element of each argument
        * The second element should be the addition of the second element of each argument
      * You are not allowed to import any module
      * You can assume that the two tuples will only contain integers
      * If a tuple is smaller than 2,
        * use the value 0 for each missing integer
      * If a tuple is bigger than 2,
        * use only the first 2 integers

##

## **No. 8. More returns!**
  * <ins>**8-multiple_returns.py**</ins>
    * <ins>**Write a function that returns a tuple with the length of a string and its first character.**</ins>
      * Prototype:
        * def multiple_returns(sentence):
      * If the sentence is empty,
        * the first character should be equal to None
      * You are not allowed to import any module

##

## **No. 9. Find the max**
  * <ins>**9-max_integer.py**</ins>
    * <ins>**Write a function that finds the biggest integer of a list.**</ins>
      * Prototype:
        * def max_integer(my_list=[]):
      * If the list is empty,
        * return None
      * You can assume that the list only contains integers
      * You are not allowed to import any module
      * You are not allowed to use the builtin max()

##

## **10. Only by 2**
  * <ins>**10-divisible_by_2.py**</ins>
    * <ins>**Write a function that finds all multiples of 2 in a list.**</ins>
      * Prototype:
        * def divisible_by_2(my_list=[]):
      * Return a new list with True or False,
        * depending on whether the integer at the same position in the original list is a multiple of 2
      * The new list should have the same size as the original list
      * You are not allowed to import any module

##

## **No. 11. ;**
  * <ins>**11-delete_at.py**</ins>
    * <ins>**Write a function that deletes the item at a specific position in a list.**</ins>
      * Prototype:
        * def delete_at(my_list=[], idx=0):
      * If idx is negative or out of range,
        * nothing change (returns the same list)
      * You are not allowed to use pop()
      * You are not allowed to import any module
##

## **No. 12. Switch**
  * <ins>**12-switch.py**</ins>
    * <ins>**Complete the source code in order to switch value of a and b**</ins>
      * Your code should be inserted where the comment is (line 4)
      * Your program should be exactly 5 lines long

##

## **No. 13. Linked list palindrome**
  * <ins>**13-is_palindrome.c, lists.h**</ins>
    * <ins>**Technical interview preparation:**</ins>
      * You are not allowed to google anything
      * Whiteboard first
    * <ins>**Write a function in C that checks if a singly linked list is a palindrome.**</ins>
      * Prototype:
        * int is_palindrome(listint_t **head);
      * Return:
        * 0 if it is not a palindrome,
        * 1 if it is a palindrome
      * An empty list is considered a palindrome

#

<h1 align="center"> ADVANCED_TASKS (Task 14)</h1>

## **14. CPython #0: Python lists**
  * <ins>**100-print_python_list_info.c**</ins>
    * CPython is the reference implementation of the Python programming language.
      * Written in C, CPython is the default and most widely used implementation of the language.
    * Since we now know a bit of C,
      * we can look at what is happening under the hood of Python.
        * Let’s have fun with Python and C, and
        * let’s look at what makes Python so easy to use.
          * All your files will be interpreted/compiled on Ubuntu 14.04 LTS
    * <ins>**Create a C function that prints some basic info about Python lists.**</ins>
      * Prototype:
        * void print_python_list_info(PyObject *p);
      * Python version:
        * 3.4
      * Your shared library will be compiled with this command line:
        * gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
      * OS:
        * Ubuntu 14.04 LTS
      * Start by reading:
        * listobject.h
        * object.h
        * Common Object Structures
        * List Objects

##
