
'''There are a few object types that we will be focusing on in this short lesson:

1. Strings = A string of characters used to make words - str()
2. Integers = Numbers that python can perform arithmetic on - int()
3. Variables = Objects that can be assigned a value - var()
4. Operators = Objects that are used to perform logic 

We will also cover basic functions and how they operate

Before all that, let's talk about comments. All of the text in this section so far has been within a comment, so Python will skip it when rendering. This is so you can
take the entirety of this code and place it directly into an IDE to run it with minimal editing. The multi-quote style that I'm using should NOT be used at this time. 
Instead, use the more common method of adding # to the beginning of a line.

NORMAL FUNCTIONS DO NOT WORK IN COMMENTS, so you can freely type whatever you like. This is a great way to notate your code for easy reference later.

For now, leave any notes in multi-quotes alone, and only worry about lines commented out with #. You will be explicitly instructed where and when to uncomment code.

#################################################################################################################################################################
#################################################################################################################################################################
#########################################################                  Introduction                   #######################################################
#################################################################################################################################################################
#################################################################################################################################################################

What is object oriented programming (OOP)? To be redundant, it simply means programming that is oriented around objects. You define a type of object, then perform 
functions based around that object. So what does all of this mean? Well, let's look at this using a metaphor.

Imagine you are talking to an alien that does not understand your language or anything about your world. For some reason, you need to tell this alien that it needs to
eat an apple. So how would you do this if the alien didn't know what apples or eating were? You would have to define both of these things so they would understand.

First, you would have to describe what an apple is to the alien. Once it understands that, you would then have to describe what eating means. This is more or less what 
you are doing with a programming language. The apple would be the object, and eating would be the function oriented around the object. Let's begin the first lesson and
explore this further.


#################################################################################################################################################################
#################################################################################################################################################################
#########################################################                     PART ONE                      #####################################################
#################################################################################################################################################################
#################################################################################################################################################################

In order to help illustrate the concept we just learned, let's run our first program!

UNCOMMENT AND RUN THE FOLLOWING CODE
Here's a tip: You can comment or uncomment a line by adding and removing the # symbol from the beginning of the line, but you can also select the line you are working
on by triple clicking, then hit Ctrl + / to comment or uncomment the whole line!'''

# IMPORTANT!!!! REMEMBER TO RE-COMMENT THE CODE AFTER YOU RUN IT! IF YOU LEAVE CODE UNCOMMENTED IN THIS LESSON IT WILL BREAK THE OTHER EXAMPLES. DO THIS EACH TIME!

#print("Hello World!")

'''Congratulations! You just wrote your first Python program! It may seem silly, since when we think of "writing a program" we imagine something robust with hundreds
or thousands of line of code, but this isn't the case. Remember, OOP is executing funcitons based on objects, which is exactly what you just did. By definition, you
wrote and executed a fully functional program. So let's start diving into exactly what we just did and what it all means.

Before we ge ino functions, let's first talk about objects.

If you remember from the beginning of the lesson, we said that you need to define an object before Python is able to perform a function on it. So how did we tell
Python what our object was? Take a second about it and think before moving on.'''

#Uncomment and run the following code:

#Hello World!


'''As you can see, when this code is run, the terminal shows "SyntaxError: invalid syntax". What does that mean? 
Syntax refers to the way that the program is written and read by the interpreter. As is the case with many human languages, programming languages may be written and read
in many different ways, as well. While you don't have cases where code is written right to left such as languages like Arabic or Hebrew, the way you structure code may
be very different.Python, and many other programming languages, read just like English, from left to right and top to bottom.

You'll notice that only the word "Hello" was highlighted here and not "World!". This is because in this case, Python has read the whitespace between these characters
as meaning that they are separate items; this is because we have not defined what these characters mean. As soon as Python read the first undefined object, the 
program crashed and never made it to the next word.

Python automatically understands the type of some objects, but many things that are typed into Python require definition, meaning you have to tell Python what type of 
object it is.

In the case of words or sentences, the type of object that we want to define is called a "String". This simply means a string of characters that are read together.
These characters can be either letters or numbers. Strings are defined by surrounding characters with either single quotes ' ' or double quotes " ".

Let's look at an example. Uncomment the following line and run the IDEw
Remember: You can also comment and uncomment by highlighting text and pressing ctrl + / OR cmd + /


DON'T FORGET TO RE-COMMENT AFTERWARDS'''

#"Hello World!"


'''This time, we had no output from the terminal. This is because Python recognized what you typed as a String. Depending on which IDE you are using, you may have also
had the color of the text change once quotes were placed, as well.

The quotes we added essenially work as an identifier to tell Python "Treat this as a string". You can see this demonstrated below.

UNCOMMENT AND RUN THE FOLLOWING CODE'''

#print(type("Hello World!"))


'''Looking at the terminal, the output was <class 'str'>. Now, don't worry yet about what a class is since we have a lot to cover before we ge to those. The important
thing to note is Python realized it was now a String, represented by 'str'. By adding the correct identifier, Python was able to determine the object type. We will 
discuss this in more detail in a bit.

So Python recognized what we typed as a String, but why was nothing done with it? This is because we did not provide any function to operate the object. Remember, in 
Object Oriented Programming (OOP), once you define an object you need to tell Python what to do with that object. Think of the eat(apple) metaphor from earlier.

Depending on what you are trying to acheive, you may need to define a function yourself, but there are a lot of functions that are built directly into Python that 
can be utilized. One of the most common built-in functions that you will use is print(). print() is used anytime you want to display information directly to the terminal. 
print() is used not only to output the results of functions, but is also invaluable for providing you with important information about how your code is run, like how we 
used type() to view the object type of our string eariler.

In the case of print, you will place whatever information you would like to be output to the terminal within the parenthesis - print(x)

Below, try writing the code yourself to print "Hello World!" to the terminal.

WRITE YOUR FUNCTION BELOW THEN COMMENT IT OUT AFTER RUNNING IT'''

# Code Goes Here


'''Congratulations! You've just written your first Python program!
Again,it may seem like a very trivial thing, just printing a few words, but defining objects and performing functions on them is the definition of what OOP is.

Ok, feeling good? Take a break and stretch if you need to. Always remember to be aware of your posture and not sitting in one spot for extended periods of time!

Alright, let's dive into strings a bit and learn more about how they work. 

UNCOMMENT AND RUN THE FOLLOWING CODE'''

#print('He said hes learning to code.')

'''Everything looks fine here and the function runs, but the sentence is gramatically incorrect. Let's change hes to he's and re-run the function.
UNCOMMENT AND RUN THE FOLLOWING CODE'''

#print('He said he's learning to code.')

'''UH-OH! We broke the program! But why did this happen? 

When Python reads anything within a container, such as quotes, it will look for opening and closing characters that are the same. When using single-quotes, Python read 
the first ' as the opening character, then interpreted the next ' it came across as the closing character. IT IS IMPORTANT TO BE CONSITENT WITH WHICH TYPES YOU USE. 
By mixing quotation types, you can inadvertently define the wrong information. This is also why you were told to avoid using multi-quote comments in the beginning of 
this lesson, as they can be hard to keep track of and may break large sections of code.

So how do we fix this? Well the first option is we could simply use alternating quotation styles to differentiate.
UNCOMMENT AND RUN THE FOLLOWING CODE'''


#print("He said he's learning to code.")


'''Here, double quotes were used to define where the string began and ended, so one single quote in the middle was not interpreted as a container. This would even work
with multiple single quotes.
UNCOMMENT AND RUN THE FOLLOWING CODE'''


print("He's always saying there's always something to learn)
      

'''Again, the single quotes were contained within double quotes, so we were fine. But what if for some reason we needed to use both types? Let's look at an example
UNCOMMENT AND RUN THE FOLLOWING CODE'''
      
#print("She's always saying "Practice makes perfect".")


'''Obviously, writing the sentence like this doesn't work. So how can we get around this? One way is using what is known as a Regular Expression. 
Regular Expressions are denoted by the "\" character, and are usually followed by a letter or symbol denoting their specific function
UNCOMMENT AND RUN THE FOLLOWING CODE'''

#print("He's always saying \"Practice makes perfect\".")

'''See how that worked? When you type a string into python, the actual text you type is referred to as the "string literal", because this is what you actually typed. The
"string value" is what is actually read as the string object.

The "\" character here essentially tells Python "This is still the string literal, please don't treat the symbol as a special character", so that qoute will now be read
as being part of the string literal. You may not use this feature too frequently, but one you will undoubtedly use often is \n or newline.
UNCOMMENT AND RUN THE FOLLOWING CODE'''


#print("Hello\nWorld!")

'''You'll see here that the output was printed onto two lines. Adding the newline regular expression told the IDE that you want whatever follows to be printed on a 
new line. You can place this anywere in the string and repeat the character multiple times for additional spacing.
UNCOMMENT AND RUN THE FOLLOWING CODE'''

#print("Hello\n\n\nWorld!")
      
'''The string was now printed with three lines separating them. Pretty cool, right? We'll explore string manipulation more in-depth later but, for now, let's take a look
at some other object types!'''



#################################################################################################################################################################
#################################################################################################################################################################
#########################################################                     PART TWO                      #####################################################
#################################################################################################################################################################
#################################################################################################################################################################

'''As we stated earlier, many different programming languges have different syntax that allows them to be read, and in many of these languages object types have to be
explicitly defined. Python tries to do most of this itself, which is a main reason why people view it as a more friendly language; it tries to determine object types
automatically as they are typed. When we defined what a string was, it really was more of us telling Python which type of object it wasn't, since many are automatically
defined. Let's look at an example.
UNCOMMENT AND RUN THE FOLLOWING CODE'''


#print(2+2)
      

'''Python was able to run this expression natively because it was able to interpret these characters without definition. Unless you define them otherwise, any numbers
that you type into Python will be read as Integers. Most languages will natively understand numbers to be integers.

THE PRIMARY DIFFERENCE BETWEEN A STR() CHARACTER AND AN INT() CHARACTER IS THAT YOU CAN PERFORM ARITHMETIC TO INTEGERS
This can be done with addition(+), subtraction(-), multiplication(*), division(/), and other mathmatical operators. Let's look at an example of the difference.
UNCOMMENT AND RUN THE FOLLOWING CODE'''

# print(2 + 3)
# print("2" + 3)
      

'''The first expression works correctly, but the second one raises a TypeError Exception:

      "TypeError: can only concantenate str (not "int") to str"

What the heck does that mean?

Because we had an integer and a string, Python tried to mathmatically add the two values, which obviously would not work due to their conflicting object types.
UNCOMMENT AND RUN THE FOLLOWING CODE'''

      #print(type("two"))
      #print(type(2))

'''When we call up the objects' types, we can see that "two" is recognized as a string, and "2" is recognized as an integer.
So what would happen if we place quotes around both of the integers?
UNCOMMENT AND RUN THE FOLLOWING CODE'''
      
      #print("2"+"3")


'''Here, we received an output of "23" because, since Python cannot perform arithmetic on strings, the actual string literals were added together. This is called
Concantenation. Concantenation is a fancy word used when we join objects instead of mathmatically adding them. Because you can't perform arithmetic on a string, 
Python will concantenate those values instead.

Concantenation can help you to format strings by combining values into one output. We will look at some more realistic examples of this is just a bit, but here's a quick
example that illustrates this concept.
UNCOMMENT AND RUN THE FOLLOWING CODE'''

#print("Hello " + "World!")
      
'''Here, we added the values of the string together but added a space between Hello and the quotes. Python took this whitespace as a part of the string literal and 
printed it out attached to Hello. This is how we were able to provide a space between the first and second literals. We'll do a few more examples in just a moment but, 
before we continue, are there any times you can combine mathmatical operators and strings? There sure are!
UNCOMMENT AND RUN THE FOLLOWING CODE'''


#print(2 * "Hello")


'''In this case, python reads this code as: 

Print --> 2x --> "Hello" 

You can think of this as "Print Hello twice". You can use this with Regular Inspections such as \n to interesting effect.
UNCOMMENT AND RUN THE FOLLOWING CODE'''


#print(2*("Hello\nWorld!"))
      

'''Python reads this as: 

Print --> 2x --> "Hello" --> (newline) --> "World!" --> "Hello" --> (newline) --> "World!"

No spaces were added in, which is why anything not told to be printed on a newline appears combined. Concantenation can be a powerful tool, and you can really see the 
benefits when working with...'''



#################################################################################################################################################################
#################################################################################################################################################################
#########################################################                    PART THREE                      ####################################################
#################################################################################################################################################################
#################################################################################################################################################################


'''Variables!

As you may remember from math class, variables are just objects used to assign a value. Think of them almost like containers, like a barrel full of water. You can put
a big label that says "WATER" on the barrel to represent its contents. Let's jump right in and look at some examples.
UNCOMMENT AND RUN THE FOLLOWING CODE'''
      
      #a = 1
      #b = 2
      #c = a + b
      #print(c)
      
'''Just like in math class, we assigned numerical values to variables, then were able to add those variables together to produce a sum. Unlike math class, however, is 
how the result is written. Notice here that we wrote "c = a + b" rather than "a + b = c". This is because Python needs to have an object before something can be assigned
to it. You need to set the variable before it can have a value. Think again about that barrel of water; you wouldn't be able to put the water inside if you didn't 
already have the barrel ready.

We can also assign different values, such as strings, to variables.
UNCOMMENT AND RUN THE FOLLOWING CODE'''


# x = "Hello"

# y = "World!"

# print(x + y)


'''Python assigned the strings as values for the variables then concantenated those values together. Notice, however, that the strings are mashedtogether without any 
space. This is because as demonstrated earlier, Python directly concantenates the values that are given. 
So how can we add spaces to make it more readable? There are two main ways to do this:'''

#UNCOMMENT AND RUN THE FOLLOWING#
# print("Hello " + "World!")

# x = "Hello"
# y = "World!"

# print(x + " " + y)


'''With the first method, we did what we covered earlier and simply added a space to the end of the first string literal. This could also have been done by 
"Hello" + " World!" since both literals are butted together no matter what. But what about the second example? Because there was no room to add whitespace here, we 
needed to concantenate an additional whitespace.

IMPORTANT!: 
" " (quotes with a space) is whitespace, while "" (quotes with no space) is an empty string. This is because, as we mentioned, whitespace is treated as part of the
string literal when within the containers. An empty string is literally a string that contains no value. 
UNCOMMENT AND RUN THE FOLLOWING CODE'''
      
      #print("Hello" + "" + "World!")
      
'''Notice how there was no space between the outer strings? This is because the string in the middle had no value, so nothing was printed in that space.


Now, we know we can't combine different object types, but sometimes you will need to! So what do we do? You can perform type conversion on some objects in order to 
change their class.
Below is an example of type conversion, utilizing the other topics covered earlier. Refer to the notes if you have questions about the function.'''


#UNCOMMENT AND RUN THE FOLLOWING#
# x = "Joe"

# y = 23

# print("Your name is " + x + " and you are " + str(y) + " years old.")


'''Our y variable was an integer, which would normally not be able to be concantenated to the strings, but by wrapping the variable in str(), we overrode Python's 
inherent classification and told it to read the variable as a string instead of an integer. You can do the same thing with integers.
UNCOMMENT AND RUN THE FOLLOWING CODE'''
      
#x = "2"
#y = "3"
#print(int(x) + int(y))

''' Here, we converted the strings to integers and were able to perform arithmetic on them. 

Let's be honest, all this type conversion and concantenation can be a bit overwhelming, especially in our "Joe", "23" example. So is there an easier way to do this 
more effectively? There sure is!

We can save ourselves a lot of typing and conversion by simply using an f-string, which is shorthand for formatted string. An f-string takes certain values and 
automatically formats them, letting you type the string like normal. 
UNCOMMENT AND RUN THE FOLLOWING CODE'''

#x = "Joe"
#y = 23

#print(f"Your name is {x} and you are {y} years old.\nNice to meet you!")

'''Way easier, right? By placing an "f" before the quotes, we told Python this was going to be a formatted string. After that, all we had to do was insert braces with 
the variable name wherever we wanted the value in the string. This not only saves a bunch of time, but cuts out a lot of the clutter.

You may not have noticed, but the code above uses strings, integers, variables, operators, regular expressions, and f-strings! Whew! In just three lines we've combined 
most of the topics we've learned throughout this lesson. 

Pretty cool! In the next lesson, we're really going to start doing the cool stuff when we begin working with functions and logic!'''
