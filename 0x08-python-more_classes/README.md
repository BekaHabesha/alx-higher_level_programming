<H1 align="center", height="1500"> <ins> README.md File </ins> </H1>
<H1 align="center", height="1500"> <ins> 0x08. Python - More Classes and Objects README.md File</ins> </H1>

![BekaHabesha.]( https://i.ibb.co/1s3X0yr/0x08-Python-More-Classes-and-Objects-Alx-logo.png)

##

* File_name: <ins>**README.md file**</ins>
* Created: <ins>**On November 27, 2023**</ins>
* Author: <ins>***Bereket Dereje Mekonnen***</ins>
* Project: <ins>**0x08. Python - More Classes and Objects**</ins>
* GitHub repository: <ins>**alx-higher_level_programming**</ins>
* Directory: <ins>**0x08-python-more_classes**</ins>
* Project Tasks: <ins>**Mandatory and Advanced**</ins>
* Tasks in number: <ins>**11 Tasks (10-Mandatory & 1-Advanced)**</ins>
* Mandatory_Tasks: <ins>**From Task 0 to 9**</ins>
* Advanced_Tasks: <ins>**Task 10**</ins>

##

### **PROJECT_TITLE:**
<h2 align="center"> <ins>0x08. Python - More Classes and Objects</ins> </h2>

### **GITHUB_REPOSITORY:**
<h2 align="center"> <ins>alx-higher_level_programming</ins> </h2>

### **DIRECTORY:**
<h2 align="center"> <ins>0x08-python-more_classes</ins> </h2>

##

<h1 align="center"> <ins>Resources</ins>:floppy_disk:</H1>

### **Read or watch:**:heavy_check_mark:
* [Object Oriented Programming](https://intranet.alxswe.com/rltoken/M-MFweENpRdEfRto_Gzlvg)(Read everything until the paragraph “Inheritance” (excluded))
* [Object-Oriented Programming](https://intranet.alxswe.com/rltoken/_Awd8Gn4SBdq2FRd_bY8KA)(Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
* [Class and Instance Attributes](https://intranet.alxswe.com/rltoken/SGQIevRxW6lTgr4jGDzXbw)
* [classmethods and staticmethods](https://intranet.alxswe.com/rltoken/Ij1EnTg02gtIknOkNv4xGA)
* [Properties vs. Getters and Setters](https://intranet.alxswe.com/rltoken/xjpk-jUNe0uGEzcNXbwIHQ)(Mainly the last part “Public instead of Private Attributes”)
* [str vs repr](https://intranet.alxswe.com/rltoken/iu1ILT-t6FMuZvk7vRvfuQ)

![My alx. ]( https://yourengineer.in/wp-content/uploads/2021/08/Python-Programming-e1628700625240.png)

<H1 align="center"><ins>Learning Objectives</ins>:floppy_disk:</H1>

* At the end of this project, You are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/hOViVT2nJU8jeBxvw52bjw), **Without the help of Google:**

![Alx.]( https://pythonweb.org/wp-content/uploads/2021/04/Programming-HD-Wallpapers-Python-And-Other-Coding-1024x576.jpg)

#

<H2> <ins>General Learning Objectives</ins>:heavy_check_mark:</H2>

* Why Python programming is awesome
* What is <ins>**OOP</ins>**
* **“first-class everything”**
* What is a <ins>**class</ins>**
* What is an <ins>**object</ins>** and an <ins>**instance</ins>**
* What is the difference between a <ins>**class</ins>** and an <ins>**object</ins>** or <ins>**instance</ins>**
* What is an <ins>**attribute</ins>**
* What are and how to use <ins>**public</ins>**, <ins>**protected</ins>** and <ins>**private attributes</ins>**
* What is <ins>**self</ins>**
* What is a <ins>**method</ins>**
* What is the special **__init__** method and how to use it
* What is <ins>**Data Abstraction</ins>**, <ins>**Data Encapsulation</ins>**, and <ins>**Information Hiding</ins>**
* What is a <ins>**property</ins>**
* What is the difference between an <ins>**attribute</ins>** and a <ins>**property</ins>** in <ins>**Python</ins>**
* What is the <ins>**Pythonic way</ins>** to <ins>**write getters</ins>** and<ins>**setters</ins>** in <ins>**Python</ins>**
* What are the special **__str__** and **__repr__** methods and how to use them
* What is the difference between **__str__** and **__repr__**
* What is a <ins>**class attribute</ins>**
* What is the difference between a <ins>**object attribute</ins>** and a <ins>**class attribute</ins>**
* What is a <ins>**class method</ins>**
* What is a <ins>**static method</ins>**
* How to <ins>**dynamically</ins>** create <ins>**arbitrary new attributes</ins>** for <ins>**existing instances</ins>** of a class
* How to <ins>**bind attributes</ins>** to <ins>**object</ins>** and <ins>**classes</ins>**
* What is and what does contain **__dict__** of a class and of an instance of a class
* How does <ins>**Python</ins>** find the <ins>**attributes</ins>** of an <ins>**object</ins>** or <ins>**class</ins>**
* How to use the <ins>**getattr</ins>** **function**

![My alx. ]( https://ciracollege.com/wp-content/uploads/2020/11/How-to-Learn-Python.jpg)

###
<H2> <ins>Copyright - Plagiarism</ins>:heavy_check_mark:</H2>

* You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
* You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
* You are not allowed to publish any content of this project.
* Any form of plagiarism is strictly forbidden and will result in removal from the program.

![Alx.]( https://img.freepik.com/premium-photo/seo-optimization-modern-tech-php-syntax-highlighted-writing-programming-functions-laptop-big-data-internet-things-trend_372999-537.jpg)

##

<H1 align="center"> <ins>Requirements</ins>:floppy_disk:</H1>

<H2><ins>General</ins> :heavy_check_mark:</H2>

* Allowed editors: <ins>**vi**</ins>, <ins>**vim**</ins>, <ins>**emacs**</ins>.
* All your files will be **interpreted/compiled** on <ins>**Ubuntu 20.04 LTS**</ins> Using <ins>**python3**</ins> (version 3.8.5)
* All your files should **end with a new line**
* The first line of all your files should be exactly <ins>**#!/usr/bin/python3**</ins>
* A <ins>**README.md file**</ins>, at the root of the folder of the project is mandatory.
* Your code should use the **pycodestyle** (version 2.8.*). 
* All **your files** must be **executable**.
* The length of your files will be tested using **wc**.

![My alx. ]( https://builtin.com/cdn-cgi/image/f=auto,quality=80,width=752,height=435/https://builtin.com/sites/www.builtin.com/files/styles/byline_image/public/2022-09/robot-code-robotics-robotic-programming-language.png)


##

* File_name: 
  * <ins>**README.md file**</ins>
* Created: 
  * <ins>**On November 27, 2023**</ins>
* Author: 
  * <ins>***Bereket Dereje Mekonnen***</ins>
* Project: 
  * <ins>**0x08. Python - More Classes and Objects**</ins>
* GitHub repository: 
  * <ins>**alx-higher_level_programming**</ins>
* Directory: 
  * <ins>**0x08-python-more_classes**</ins>
* Project Tasks: 
  * <ins>**Mandatory and Advanced**</ins>
* Tasks in number: 
  * <ins>**11 Tasks (10-Mandatory & 1-Advanced)**</ins>
* Mandatory_Tasks: 
  * <ins>**From Task 0 to 9**</ins>
* Advanced_Tasks: 
  * <ins>**Task 10**</ins>

##

![BekaHabesha.]( https://i.ibb.co/y5wmQyd/Alx-enginn-Build-ur-future.png)

<H1 align="center"> <ins> PROJECT TASKS (Mandatory and Advanced)</ins>:floppy_disk:</H1>

<H1 align="center">MANDATORY_TASKS (From Task 0 to 9):cd:</h1>

## **No. 0. Simple rectangle**:heavy_check_mark:
* File:
  * <ins>**0-rectangle.py**</ins>
###
* Write an **empty class** <ins>**Rectangle**</ins> that defines a **rectangle:**
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/P1ZydRN/0-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **No test cases needed.**

##

## **No. 1. Real definition of a rectangle**:heavy_check_mark:
* File:
  * <ins>**1-rectangle.py**</ins>
###
* * Write a **class** <ins>**Rectangle**</ins> that defines a **rectangle** by: (based on **</ins>0-rectangle.py**</ins>)
  * <ins>***Private instance attribute</ins>:*** **width:**
    * property <ins>**def width(self)</ins>:**  to retrieve it
    * property setter <ins>**def width(self, value)</ins>:**  to set it:
      * <ins>**width**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**width must be an integer**</ins>
      * If <ins>**width**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**width must be >= 0**</ins>
###
  * <ins>***Private instance attribute</ins>:*** **height:**
    * property <ins>**def height(self)</ins>:**  to retrieve it
    * property setter <ins>**def height(self, value)</ins>:**  to set it:
      * <ins>**height**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**height must be an integer**</ins>
      * If <ins>**height**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**height must be >= 0**</ins>
###
  * Instantiation with optional <ins>**width**</ins> and <ins>**height</ins>:** **def __init__(self, width=0, height=0):**
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/zmLgvnb/1-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **No test cases needed.**

##

## **No. 2. Area and Perimeter**:heavy_check_mark:
* File:
  * <ins>**2-rectangle.py**</ins>
###
* Write a **class** <ins>**Rectangle**</ins> that defines a **rectangle** by: (based on **</ins>1-rectangle.py**</ins>)
  * <ins>***Private instance attribute</ins>:*** **width:**
    * property <ins>**def width(self)</ins>:**  to retrieve it
    * property setter <ins>**def width(self, value)</ins>:**  to set it:
      * <ins>**width**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**width must be an integer**</ins>
      * If <ins>**width**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**width must be >= 0**</ins>
###
  * <ins>***Private instance attribute</ins>:*** **height:**
    * property <ins>**def height(self)</ins>:**  to retrieve it
    * property setter <ins>**def height(self, value)</ins>:**  to set it:
      * <ins>**height**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**height must be an integer**</ins>
      * If <ins>**height**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**height must be >= 0**</ins>
###
  * Instantiation with optional <ins>**width**</ins> and <ins>**height</ins>:** **def __init__(self, width=0, height=0):**
  * **Public instance method:** <ins>**def area(self)</ins>:** that returns the **rectangle area**
  * **Public instance method:** <ins>**def perimeter(self)</ins>:** that returns the **rectangle perimeter:**
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **perimeter** is equal to <ins>**0**</ins>
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/dgwdXvd/2-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **No test cases needed.**

##

## **No. 3. String representation**:heavy_check_mark:
* File:
  * <ins>**3-rectangle.py**</ins>
###
* Write a **class** <ins>**Rectangle**</ins> that defines a **rectangle** by: (based on **</ins>2-rectangle.py**</ins>)
  * <ins>***Private instance attribute</ins>:*** **width:**
    * property <ins>**def width(self)</ins>:**  to retrieve it
    * property setter <ins>**def width(self, value)</ins>:**  to set it:
      * <ins>**width**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**width must be an integer**</ins>
      * If <ins>**width**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**width must be >= 0**</ins>
###
  * <ins>***Private instance attribute</ins>:*** **height:**
    * property <ins>**def height(self)</ins>:**  to retrieve it
    * property setter <ins>**def height(self, value)</ins>:**  to set it:
      * <ins>**height**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**height must be an integer**</ins>
      * If <ins>**height**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**height must be >= 0**</ins>
###
  * Instantiation with optional <ins>**width**</ins> and <ins>**height</ins>:** **def __init__(self, width=0, height=0):**
  * **Public instance method:** <ins>**def area(self)</ins>:** that returns the **rectangle area**
  * **Public instance method:** <ins>**def perimeter(self)</ins>:** that returns the **rectangle perimeter:**
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **perimeter** is equal to <ins>**0**</ins>
  * <ins>**print()</ins>** and <ins>**str()</ins>** should print the rectangle with the character **#:** (see example below)
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **return** an <ins>**empty string**</ins>
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/XbqRc6w/3-1-main-0x08-Python-More-Classes-and-Objects.png)
![Beki Habesha.]( https://i.ibb.co/72jp1jb/3-2-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **Object address can be different**
> **No test cases needed.**


##

## **No. 4. Eval is magic**:heavy_check_mark:
* File:
  * <ins>**4-rectangle.py**</ins>
###
* Write a **class** <ins>**Rectangle**</ins> that defines a **rectangle** by: (based on **</ins>3-rectangle.py**</ins>)
  * <ins>***Private instance attribute</ins>:*** **width:**
    * property <ins>**def width(self)</ins>:**  to retrieve it
    * property setter <ins>**def width(self, value)</ins>:**  to set it:
      * <ins>**width**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**width must be an integer**</ins>
      * If <ins>**width**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**width must be >= 0**</ins>
###
  * <ins>***Private instance attribute</ins>:*** **height:**
    * property <ins>**def height(self)</ins>:**  to retrieve it
    * property setter <ins>**def height(self, value)</ins>:**  to set it:
      * <ins>**height**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**height must be an integer**</ins>
      * If <ins>**height**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**height must be >= 0**</ins>
###
  * Instantiation with optional <ins>**width**</ins> and <ins>**height</ins>:** **def __init__(self, width=0, height=0):**
  * **Public instance method:** <ins>**def area(self)</ins>:** that returns the **rectangle area**
  * **Public instance method:** <ins>**def perimeter(self)</ins>:** that returns the **rectangle perimeter:**
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **perimeter** is equal to <ins>**0**</ins>
  * <ins>**print()</ins>** and <ins>**str()</ins>** should print the rectangle with the character **#:** (see example below)
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **return** an <ins>**empty string**</ins>
  * <ins>**str()</ins>** should return a **string** representation of the **rectangle** to be able to recreate a new instance by using <ins>**eval()</ins>** (see example below)
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/r58CbRc/4-1-main-0x08-Python-More-Classes-and-Objects.png)
![Beki Habesha.]( https://i.ibb.co/YdKLbRH/4-2-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **No test cases needed.**

##

## **No. 5. Detect instance deletion**:heavy_check_mark:
* File:
  * <ins>**5-rectangle.py**</ins>
###
* Write a **class** <ins>**Rectangle**</ins> that defines a **rectangle** by: (based on **</ins>4-rectangle.py**</ins>)
  * <ins>***Private instance attribute</ins>:*** **width:**
    * property <ins>**def width(self)</ins>:**  to retrieve it
    * property setter <ins>**def width(self, value)</ins>:**  to set it:
      * <ins>**width**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**width must be an integer**</ins>
      * If <ins>**width**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**width must be >= 0**</ins>
###
  * <ins>***Private instance attribute</ins>:*** **height:**
    * property <ins>**def height(self)</ins>:**  to retrieve it
    * property setter <ins>**def height(self, value)</ins>:**  to set it:
      * <ins>**height**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**height must be an integer**</ins>
      * If <ins>**height**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**height must be >= 0**</ins>
###
  * Instantiation with optional <ins>**width**</ins> and <ins>**height</ins>:** **def __init__(self, width=0, height=0):**
  * **Public instance method:** <ins>**def area(self)</ins>:** that returns the **rectangle area**
  * **Public instance method:** <ins>**def perimeter(self)</ins>:** that returns the **rectangle perimeter:**
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **perimeter** is equal to <ins>**0**</ins>
  * <ins>**print()</ins>** and <ins>**str()</ins>** should print the rectangle with the character **#:** (see example below)
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **return** an <ins>**empty string**</ins>
  * <ins>**repr()</ins>** should return a **string** representation of the **rectangle** to be able to recreate a new instance by using <ins>**eval()</ins>**
  * Print the message <ins>**Bye rectangle... (...</ins>** being 3 dots not ellipsis) when an instance of <ins>**Rectangle**</ins> is deleted
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/55t4GmH/5-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **No test cases needed.**

##

## **No. 6. How many instances**:heavy_check_mark:
* File:
  * <ins>**6-rectangle.py**</ins>
###
* Write a **class** <ins>**Rectangle**</ins> that defines a **rectangle** by: (based on **</ins>5-rectangle.py**</ins>)
  * <ins>***Private instance attribute</ins>:*** **width:**
    * property <ins>**def width(self)</ins>:**  to retrieve it
    * property setter <ins>**def width(self, value)</ins>:**  to set it:
      * <ins>**width**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**width must be an integer**</ins>
      * If <ins>**width**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**width must be >= 0**</ins>
###
  * <ins>***Private instance attribute</ins>:*** **height:**
    * property <ins>**def height(self)</ins>:**  to retrieve it
    * property setter <ins>**def height(self, value)</ins>:**  to set it:
      * <ins>**height**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**height must be an integer**</ins>
      * If <ins>**height**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**height must be >= 0**</ins>
###
  * <ins>***Public class attribute</ins>:*** **number_of_instances:**
    * Initialized to <ins>**0</ins>**
    * <ins>**Incremented</ins>** during each <ins>**new instance instantiation</ins>**
    * <ins>**Decremented</ins>** during each <ins>**instance deletion</ins>**
###
  * Instantiation with optional <ins>**width**</ins> and <ins>**height</ins>:** **def __init__(self, width=0, height=0):**
  * **Public instance method:** <ins>**def area(self)</ins>:** that returns the **rectangle area**
  * **Public instance method:** <ins>**def perimeter(self)</ins>:** that returns the **rectangle perimeter:**
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **perimeter** is equal to <ins>**0**</ins>
  * <ins>**print()</ins>** and <ins>**str()</ins>** should print the rectangle with the character **#:** (see example below)
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **return** an <ins>**empty string**</ins>
  * <ins>**repr()</ins>** should return a **string** representation of the **rectangle** to be able to recreate a new instance by using <ins>**eval()</ins>**
  * Print the message <ins>**Bye rectangle... (...</ins>** being 3 dots not ellipsis) when an instance of <ins>**Rectangle**</ins> is deleted
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/XYr9H3S/6-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **No test cases needed.**

##

## **No. 7. Change representation**:heavy_check_mark:
* File:
  * <ins>**7-rectangle.py**</ins>
###
* Write a **class** <ins>**Rectangle**</ins> that defines a **rectangle** by: (based on **</ins>6-rectangle.py**</ins>)
  * <ins>***Private instance attribute</ins>:*** **width:**
    * property <ins>**def width(self)</ins>:**  to retrieve it
    * property setter <ins>**def width(self, value)</ins>:**  to set it:
      * <ins>**width**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**width must be an integer**</ins>
      * If <ins>**width**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**width must be >= 0**</ins>
###
  * <ins>***Private instance attribute</ins>:*** **height:**
    * property <ins>**def height(self)</ins>:**  to retrieve it
    * property setter <ins>**def height(self, value)</ins>:**  to set it:
      * <ins>**height**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**height must be an integer**</ins>
      * If <ins>**height**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**height must be >= 0**</ins>
###
  * <ins>***Public class attribute</ins>:*** **number_of_instances:**
    * Initialized to <ins>**0</ins>**
    * <ins>**Incremented</ins>** during each <ins>**new instance instantiation</ins>**
    * <ins>**Decremented</ins>** during each <ins>**instance deletion</ins>**
###
  * <ins>***Public class attribute</ins>:*** **print_symbol:**
    * Initialized to <ins>**#</ins>**
    * Used as <ins>**symbol</ins>** for <ins>**string representation</ins>**
    * Can be <ins>**any type</ins>**
###
  * Instantiation with optional <ins>**width**</ins> and <ins>**height</ins>:** **def __init__(self, width=0, height=0):**
  * **Public instance method:** <ins>**def area(self)</ins>:** that returns the **rectangle area**
  * **Public instance method:** <ins>**def perimeter(self)</ins>:** that returns the **rectangle perimeter:**
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **perimeter** is equal to <ins>**0**</ins>
  * <ins>**print()</ins>** and <ins>**str()</ins>** should print the rectangle with the character **#:** (see example below)
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **return** an <ins>**empty string**</ins>
  * <ins>**repr()</ins>** should return a **string** representation of the **rectangle** to be able to recreate a new instance by using <ins>**eval()</ins>**
  * Print the message <ins>**Bye rectangle... (...</ins>** being 3 dots not ellipsis) when an instance of <ins>**Rectangle**</ins> is deleted
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/Z8XPwZf/7-1-main-0x08-Python-More-Classes-and-Objects.png)
![Beki Habesha.]( https://i.ibb.co/bzNTMCH/7-2-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **No test cases needed.**

##

## **No. 8. Compare rectangles:
* File:
  * <ins>**8-rectangle.py**</ins>
###
* Write a **class** <ins>**Rectangle**</ins> that defines a **rectangle** by: (based on **</ins>7-rectangle.py**</ins>)
  * <ins>***Private instance attribute</ins>:*** **width:**
    * property <ins>**def width(self)</ins>:**  to retrieve it
    * property setter <ins>**def width(self, value)</ins>:**  to set it:
      * <ins>**width**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**width must be an integer**</ins>
      * If <ins>**width**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**width must be >= 0**</ins>
###
  * <ins>***Private instance attribute</ins>:*** **height:**
    * property <ins>**def height(self)</ins>:**  to retrieve it
    * property setter <ins>**def height(self, value)</ins>:**  to set it:
      * <ins>**height**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**height must be an integer**</ins>
      * If <ins>**height**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**height must be >= 0**</ins>
###
  * <ins>***Public class attribute</ins>:*** **number_of_instances:**
    * Initialized to <ins>**0</ins>**
    * <ins>**Incremented</ins>** during each <ins>**new instance instantiation</ins>**
    * <ins>**Decremented</ins>** during each <ins>**instance deletion</ins>**
###
  * <ins>***Public class attribute</ins>:*** **print_symbol:**
    * Initialized to <ins>**#</ins>**
    * Used as <ins>**symbol</ins>** for <ins>**string representation</ins>**
    * Can be <ins>**any type</ins>**
###
  * Instantiation with optional <ins>**width**</ins> and <ins>**height</ins>:** **def __init__(self, width=0, height=0):**
  * **Public instance method:** <ins>**def area(self)</ins>:** that returns the **rectangle area**
  * **Public instance method:** <ins>**def perimeter(self)</ins>:** that returns the **rectangle perimeter:**
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **perimeter** is equal to <ins>**0**</ins>
  * <ins>**print()</ins>** and <ins>**str()</ins>** should print the rectangle with the character **#:** (see example below)
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **return** an <ins>**empty string**</ins>
  * <ins>**repr()</ins>** should return a **string** representation of the **rectangle** to be able to recreate a new instance by using <ins>**eval()</ins>**
  * Print the message <ins>**Bye rectangle... (...</ins>** being 3 dots not ellipsis) when an instance of <ins>**Rectangle**</ins> is deleted
  * <ins>**Static method</ins>** **def bigger_or_equal(rect_1, rect_2):** that **returns** the <ins>**biggest rectangle</ins>** based on the <ins>**area</ins>**
    * **rect_1** must be an instance of <ins>**Rectangle**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message **rect_1 <ins>must be an instance of Rectangle**</ins>
    * **rect_2** must be an instance of <ins>**Rectangle**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message **rect_2 <ins>must be an instance of Rectangle**</ins>
    * Returns **rect_1** if both have the <ins>**same area value**</ins>
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/B40NGWL/8-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **No test cases needed.**

##

## **No. 9. A square is a rectangle**:heavy_check_mark:
* File:
  * <ins>**9-rectangle.py**</ins>
###
* Write a **class** <ins>**Rectangle**</ins> that defines a **rectangle** by: (based on **</ins>8-rectangle.py**</ins>)
  * <ins>***Private instance attribute</ins>:*** **width:**
    * property <ins>**def width(self)</ins>:**  to retrieve it
    * property setter <ins>**def width(self, value)</ins>:**  to set it:
      * <ins>**width**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**width must be an integer**</ins>
      * If <ins>**width**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**width must be >= 0**</ins>
###
  * <ins>***Private instance attribute</ins>:*** **height:**
    * property <ins>**def height(self)</ins>:**  to retrieve it
    * property setter <ins>**def height(self, value)</ins>:**  to set it:
      * <ins>**height**</ins> must be an <ins>**integer**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message <ins>**height must be an integer**</ins>
      * If <ins>**height**</ins> is less than <ins>**0**</ins>, raise a <ins>**ValueError**</ins> exception with the message <ins>**height must be >= 0**</ins>
###
  * <ins>***Public class attribute</ins>:*** **number_of_instances:**
    * Initialized to <ins>**0</ins>**
    * <ins>**Incremented</ins>** during each <ins>**new instance instantiation</ins>**
    * <ins>**Decremented</ins>** during each <ins>**instance deletion</ins>**
###
  * <ins>***Public class attribute</ins>:*** **print_symbol:**
    * Initialized to <ins>**#</ins>**
    * Used as <ins>**symbol</ins>** for <ins>**string representation</ins>**
    * Can be <ins>**any type</ins>**
###
  * Instantiation with optional <ins>**width**</ins> and <ins>**height</ins>:** **def __init__(self, width=0, height=0):**
  * **Public instance method:** <ins>**def area(self)</ins>:** that returns the **rectangle area**
  * **Public instance method:** <ins>**def perimeter(self)</ins>:** that returns the **rectangle perimeter:**
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **perimeter** is equal to <ins>**0**</ins>
  * <ins>**print()</ins>** and <ins>**str()</ins>** should print the rectangle with the character **#:** (see example below)
    * If <ins>**width**</ins> or <ins>**height**</ins> is equal to <ins>**0**</ins>, **return** an <ins>**empty string**</ins>
  * <ins>**repr()</ins>** should return a **string** representation of the **rectangle** to be able to recreate a new instance by using <ins>**eval()</ins>**
  * Print the message <ins>**Bye rectangle... (...</ins>** being 3 dots not ellipsis) when an instance of <ins>**Rectangle**</ins> is deleted
  * <ins>**Static method</ins>** **def bigger_or_equal(rect_1, rect_2):** that **returns** the <ins>**biggest rectangle</ins>** based on the <ins>**area</ins>**
    * **rect_1** must be an instance of <ins>**Rectangle**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message **rect_1 <ins>must be an instance of Rectangle**</ins>
    * **rect_2** must be an instance of <ins>**Rectangle**</ins>, otherwise raise a <ins>**TypeError**</ins> exception with the message **rect_2 <ins>must be an instance of Rectangle**</ins>
    * Returns **rect_1** if both have the <ins>**same area value**</ins>
  * <ins>**Class method</ins>** **def square(cls, size=0):** that **returns** a new <ins>**Rectangle instance</ins>** with <ins>**width == height == size</ins>**
  * You are not allowed to <ins>**import any module**</ins>

![Beki Habesha.]( https://i.ibb.co/YZwH1zC/9-main-0x08-Python-More-Classes-and-Objects.png)

> [!NOTE]
> **No test cases needed.**

#

<h1 align="center"> ADVANCED_TASKS (From Task 6 to 8):cd:</h1>

## **No. 10. N queens**:heavy_check_mark:
* File:
  * <ins>**101-nqueens.py**</ins>

![Beki Habesha.]( http://www.crestbook.com/files/Judit-photo1_602x433.jpg)
<br>Chess grandmaster [Judit Polgár](https://intranet.alxswe.com/rltoken/bsRwbt64OvYjWaClriv0jg), the strongest female chess player of all time
###
* The <ins>**N queens puzzle**</ins> the challenge of placing **<ins>N non-attacking queens**</ins> on an **<ins>N×N chessboard**</ins>. 
  * Write a **<ins>program**</ins> that solves the **</ins>N queens problem**</ins>.
###
  * <ins>**Usage</ins>:** **nqueens N**
    * If the <ins>**user**</ins> called the <ins>**program</ins>** with the <ins>**wrong number of arguments</ins>**, 
      * print <ins>**Usage: nqueens N<ins>**, followed by a **new line**, and **exit** with the status <ins>**1</ins>**
####
  * where <ins>**N</ins>** must be an **integer <ins>greater</ins> or <ins>equal</ins> to** <ins>4</ins>
    * If <ins>**N**</ins> is not an <ins>**integer</ins>**, 
      * print <ins>**N must be a number**, followed by a **new line**, and **exit** with the status <ins>**1</ins>**
    * If <ins>**N**</ins> is <ins>**smaller than 4</ins>**, 
      * print <ins>**N must be at least 4**, followed by a **new line**, and **exit** with the status <ins>**1</ins>**
####
  * The <ins>**program</ins>** should **print <ins>every possible solution</ins> to the <ins>probleml</ins>**
    * **One solution <ins>per line**</ins>
    * **Format: <ins>see example**</ins>
    * **You don’t have to <ins>print the solutions</ins> in a <ins>specific order**</ins>
####
  * **You are only allowed to import the <ins>sys module**</ins>
####
* <ins>***Read</ins>:*** [Queen](https://intranet.alxswe.com/rltoken/dAQmi8RxMnLH-iHBzkz-lw),   [Backtracking](https://intranet.alxswe.com/rltoken/TGXZXdY2Awg8m4mSjlrjjA)
 
![Beki Habesha.]( https://i.ibb.co/WBWzkRQ/10-main-0x08-Python-More-Classes-and-Objects.png)

#
