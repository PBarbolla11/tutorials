
'''There are a few object types that we will be focusing on in this short lesson:

1. Strings = A string of characters used to make words - str()
2. Integers = Numbers that python can perform arithmetic on - int()
3. Variables = Objects that can be assigned a value - var()
4. Operators = Objects that are used to perform logic 

We will also cover basic functions and how they operate

Before all that, let's talk about comments. All of the text in this section so far has been within a comment, so Python will skip it when rendering.
The multi-quote style that I'm using should NOT be used at this time. Instead, use the more common method of adding # to the beginning of a line.

NORMAL FUNCTIONS DO NOT WORK IN COMMENTS, so you can freely type whatever you like. This is a great way to notate your code for easy reference later.

For now, leave any notes in multi-quotes alone, and only worry about lines commented out with #


Let's start the lesson by printing "Hello World!" to the terminal.
Now, uncomment the next line by removing the # and run the IDE. Look to the terminal to see what the result is.'''



#Hello World!



"""As you can see, when this is run the terminal shows "SyntaxError: invalid syntax". What does that mean? 
Syntax refers to the way that the program is written. Python, and many other programming languages, read just like you, from left to right and top to bottom.
You'll notice that only the word "Hello" was highlighted here and not "World!". This is because in this case, Python has read the whitespace between these characters
as meaning that they are separate items; this is because we have not defined what these characters mean.
Many things that are typed into Python require definition, meaning you have to tell the interpreter what type of object it is.


PART ONE


In the case of words or sentences, the type of object that we want to define is called a "String". This simply means a string of characters that are read together.
These characters can be either letters or numbers. Strings are defined by surrounding characters with either single quotes ' ' or double quotes " ".

Let's look at an example. Uncomment the following line and run the IDE
Note: You can also comment and uncomment by highlighting text and pressing ctrl + / OR cmd + /


DON'T FORGET TO RE-COMMENT AFTERWARDS"""



#"Hello World!"




'''This time, we had no output from the terminal. This is because Python recognized what you typed as a String. Depending on which IDE you are using, you may have also
had the color of the text change, as well.

So Python recognized what we typed as a String, but why was nothing done with it? This is because we did not provide any function to operate the object.
Depending on what you are trying to acheive, you may need to define a function yourself, but there are a lot of functions that are built directly into Python that 
can be utilized. One of the most common built-in functions that you will use is print().

print() is used anytime you want to display information directly to the terminal. In the case of print, you will place whatever information you would like to be 
output to the terminal within the parenthesis - print(x)

Below, write Hello World within a print function and run the IDE.



#write the function here#



Congratulations! You've just written your first Python program!
It may seem like a very trivial thing, just printing a few words, but that is the basis of what Object Oriented Programming is. Taking objects and performing functions
is the definition of what OOP is.

Let's take a closer look at Strings for a moment. Uncomment the next line and run the interpreter.'''

#UNCOMMENT AND RUN#print('He said he's learning to code.')

'''Everything looks fine here, but the sentence is gramatically incorrect. Change hes to he's and re-run the IDE.
UH-OH! We broke the program! But why did this happen? 

When Python reads anything that is "nested", it will look for opening and closing characters. When using single-quotes, Python read the first ' as the opening character,
then interpreted the next ' it came across as the closing character. IT IS IMPORTANT TO BE CONSITENT WITH WHICH TYPES YOU USE. By mixing quotes, you can inadvertently
define the wrong information. This is also why you were told to avoid using multi-quote comments in the beginning of this lesson.

So how do we fix this? Well first, we could simply use alternating quotation styles to differentiate.'''


#UNCOMMENT AND RUN# print("He said he's learning to code.")



'''By running that command, you can see that the text was now output correctly. But what if both types of quotes need to be used?'''


#UNCOMMENT AND RUN# print("He's always saying "Practice makes perfect".")


'''Notice that this doesn't work. So how can we get around this? One way is using what is known as a Regular Expression. 
Regular Expressions are denoted by the "\" character. As you can see, Python read the character immediately following the \" differently than
the rest of the comments. The reason that this did not show as an error is exactly its function. '''


#UNCOMMENT AND RUN# print("He's always saying \"Practice makes perfect\".")

'''By putting a backslash in front of the quotes, you've told Python that this is just a regular expression, and that any function that it may normally have should be ignored.
Regular Expressions can also have their own function in some cases. One of the most common examples in newline'''


#UNCOMMENT AND RUN#print("Hello\nWorld!")

'''You'll see here that the output was printed onto two lines. Adding the newline regular expression told the IDE that you want whatever follows to be printed on a new line.



PART TWO

There are some things that Python inherently understands when they are typed into the IDE. Some of the most common examples are Integers and Operators'''


#UNCOMMENT AND RUN#print(2+2)

'''Python was able to run this expression natively because it was able to interpret these characters without definition. Unless you define them otherwise, any numbers
that you type into Python will be read as Integers. 
This can be with addition(+), subtraction(-), multiplication(*), division(/), and many other operators

THE DIFFERENCE BETWEEN A STR() CHARACTER AND AN INT() CHARACTER IS THAT YOU CAN PERFORM ARITHMETIC TO INTEGERS
Let's look at an example of what we mean.'''

#UNCOMMENT AND RUN THE FOLLOWING#
# print(2 + 3)
# print("2" + 3)

'''The first expression works correctly, but the second one throws raises a TypeError Exception
"TypeError: can only concantenate str (not "int") to str"
What the heck does that mean?

Concantenation is a fancy word used when we join objects instead of adding them. Because you can't perform arithmetic on a string, Python will concantenate those values instead.'''

#UNCOMMENT AND RUN#print("2" + "3")

'''The result of this was 23 because the values were joined (concantenated) together instead of added. One interesting thing about this is that some operators can be used in 
conjunction with strings'''


#UNCOMMENT AND RUN#print(2 * "Hello")


'''In this case, python reads this as Print --> 2x --> "Hello". You can use this with Regular Inspections to interesting effect'''


#print(2*("Hello\nWorld!"))

'''Python reads this as Print --> 2x --> "Hello" --> newline --> "World!" --> "Hello" --> newline --> "World!"

While this last example may not have much practical use, concantenations are particularly helpful when working with...


PART THREE

Variables, as you may know, are just anything used to assign a value to.
Look at the following example:'''


#UNCOMMENT AND RUN THE FOLLOWING#
# x = "Hello"

# y = "World!"

# print(x + y)


'''We defined x and y by setting them equal to a string, but they can be set to many different types of objects. 
Python saw that these were variables were assigned strings and concantenated the values that were assigned. Notice, however, that the strings are mashed
together without any space. This is because Python directly concantenates the values that are given. So how can we add spaces to make it more readable?
There are two main ways to do this:'''

#UNCOMMENT AND RUN THE FOLLOWING#
# print("Hello " + "World!")

# x = "Hello"
# y = "World!"

# print(x + " " + y)


'''With the first method, we added a space simply by adding whitespace to the end of the first string. This could also have been done by "Hello" + " World!"
Because there was no room to add whitespace to the second expression, we needed to concantenate an additional whitespace.

NOTE: " " is whitespace, "" is an empty string. This is very important, as you will sometimes need to pass empty strings to be changed later.


So what if we need to perform an operation where we have two different character types? You can perform type conversion on a character type in order to change the
way it is read by Python.
Below is an example of type conversion, utilizing the other topics covered earlier. Refer to the notes if you have questions about the function.'''


#UNCOMMENT AND RUN THE FOLLOWING#
# x = "Joe"

# y = 23

# print("Your name is " + x + " and you are " + str(y) + " years old.")


'''Our y variable was an integer, which would normally not be able to be concantenated to the strings, but by wrapping the variable in str(), we told Python to read the
variable as a string instead of an integer.

Even though it was only three lines, the code above uses strings, integers, variables, and operators to acheive its function. Let's practice this a little more, but 
place everything inside a function.'''

def func():
	x = "Joe"
	y = 23

	message = ("Your name is " + x + " and you are " + str(y) + " years old.")
	print(message)

func()

'''
def function():
	pass

This is the standard format for how you will define a function. 

The next lesson will cover functions more in-depth and will also begin to cover basic logic functions.