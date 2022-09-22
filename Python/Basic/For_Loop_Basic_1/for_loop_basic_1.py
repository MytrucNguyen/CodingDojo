# Basic - Print all integers from 0 to 150.

print('~~~~~~~~~~~~~~~ 1 ~~~~~~~~~~~~~~~')
def print_all_integers(integer_range):
    for num in range(integer_range+1):
        print(num)

print_all_integers(150)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

print('~~~~~~~~~~~~~~~ 2 ~~~~~~~~~~~~~~~')
def multiples_of_five(integer_range):
    for num in range(5, integer_range+1):
        if num % 5 == 0:
            print(num)

multiples_of_five(1_000)

# Counting, the Dojo Way - Print integers 1 to 100. 
# If divisible by 5, print "Coding" instead.
# If divisible by 10, print "Coding Dojo".

print('~~~~~~~~~~~~~~~ 3 ~~~~~~~~~~~~~~~')
def dojo_way(integer_range):
    for num in range(1, integer_range+1):
        if num % 10 == 0:
            print('Coding Dojo')
        elif num % 5 == 0:
            print('Coding')
        else:
            print(num)
dojo_way(100)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

print('~~~~~~~~~~~~~~~ 4 ~~~~~~~~~~~~~~~')
def sumTotal(integer_range):
    sum = 0
    for num in range(integer_range+1):
        if num % 2 == 1:
            sum += num
    print(sum)

sumTotal(500_000)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

print('~~~~~~~~~~~~~~~ 5 ~~~~~~~~~~~~~~~')
def count_down(starting):
    for num in range(starting, 0, -4):
        print(num)

count_down(2_018)

# Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers 
# that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)
print('~~~~~~~~~~~~~~~ 6 ~~~~~~~~~~~~~~~')
def flexibleCounter(lowNum, highNum, mult):
    for num in range(lowNum, highNum+1):
        if num % mult == 0:
            print(num)

flexibleCounter(2, 9, 3)