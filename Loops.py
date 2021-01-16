#For loops-->repeatable runs through a section of code
#using range() python will halt the loop one number before the final number#ex when looping from 0-5, code will run 5 times but x will only ever be printed as 0-4
#when provided with a single number, range() will always start the loop at 0
# when provided with 2 numbers, the code will loop from the 1st until it reaches one less thant the second number

# loop through a rand of numbers(0-4)
#for x in range(5)
#list(range(5)) will output= [0, 1, 2, 3, 4]
#range(2,7)=output 2-6
#ex start with for then iterator
for x in range(5):#indent-->loop is changing each time.
    for x in range (2,7):
        print(x)

word = "peace"
for characters in word:
    print(characters)

#for statements are follosed by an item or variable that is found in a list of items of an unknown number
#-->items can be a list, tuple, or dictionary
#1st iteration-->item willbe the first item in a list
#2nd iteration-->item will be the second item on the list...ect
#the statements that follow will be executed as long as the number of items is not exhausted
##for loop stops when no more items in list

# Ex built-in range function-->creates an iterable object or list

numbers = [0, 1, 2, 3, 4]
for num in numbers:
        print(num)
    #output 0,1,2,3,4
#-->same output if simplify code by using for loop using range
for num in range(5):
        print(num)

#Indexing used to iterate through ist-->if list contains stings-->need to get length of list as integer for range()
