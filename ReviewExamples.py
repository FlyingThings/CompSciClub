#importing gives you access to other code and functions not
#always availible
import random

# the '#' symbol is a comment, meaning these words are ignored!!!
#Datatypes
x = 1#integer
t = 2.0#float(or decimal)\
robot = 'I have become setient'#string
Students = ['Nathan', 'Tyler', 'Eric', 'Julia', 'John', 'Jonas']#list

#'print' prints to the terminal the string given
print('a string is a set of characters wrapped by single or double quotes')

#Comparators
#Use <,>,==,'or', and 'and' to compare items
if(3>2):
    print('i aint that dumb')
if('True' == True):
    print('well maybe that harder')
#and comparing both have to be True to be True
if(True and False):
    print('will this ever print?')

#or comparting just has to have one be True to be True
if(True or False):
    print('prints everytime :)')

#Functions
#a function will do the lines under it until there are no more
#indents
def happyValentinesDay():
    print('you are one day late')
    print('but computers will always love you!')
#this is a function that takes a parameter 'name' and uses it as a
#variable
def hello(name):
    print('hello ' + name)
#to call a function, type its name with paratheses:
happyValentinesDay()
#to give it a value type its name and the value in paratheses:
hello('nathan')
#be careful on what type of value you input


#loops
#redo something a number of times
for h in range(1,99):
    print('this is line ' + h)

#calling a function from a library
#use import name and a method from the package
random.randint(1,6)
#randint is the method
