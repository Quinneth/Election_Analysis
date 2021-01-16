#if-else-elif-->used to create conditionals pay attention to letter case and spelling
# conclude with :, (code block) but indentation important-->all lines after colon must be indented
# multiple logic tests can be checked within single condiational statement; 
# "and" must mean both tests are true
"or" means only 1 tests returns true
#elif used to include multiple conditional expressions between if and else--
#elif is executed if the specified condition is true
#elif to add formula, if else to answers true or false
x=1
y=10

#is x=y?

if x== y:#use tab or 4 spaces to indent code block
    print('x is equal to y')# false will pass by
else
    print(' is not equal to y')

if y = 11:
    print('y is not equal to 11')

# if NOT equal to
if y != 11: #becomes false
    print('y is not equal to 11')
# 2 conditions
# if greater than
if x > 5 and x < 10: # and states it must meet both conditions
    print('x is greater than 5 and less than 10')

#meet 1 of the conditions-->use or
if x > or x < 10:
    print('x is greater than 5 or less than 10')

elif x < 2
    print('x is greater than 2')
else: 
    print ('x is zero or negative')