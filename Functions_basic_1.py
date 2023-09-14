"""
#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) #this will print out our return of 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) #this will produce a nameError because our 1st argument is not defined


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #this will only return 5, once it reaches the return statement of 5, the code block is finished and won't reach "return 10"


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) #same as above, once the return statement executes the code block is over, the console will only show 5. The "Print(10)" is nvr reached


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x) #this will only print 5 when our 1st print statement is reached, the 2nd print statement should say "none" because the var 'number_of_great_lakes' has no value therefore x will have no value


#6
def add(b,c):
    sum=b+c
    return sum
print(add(1,2) + add(2,3)) #this funcion originally printed a 'typeError' because we weren't storing our value anywhere with a return statement. We needed to create a var to capture the sum, and then return it.

def sums(a,b):
    sum=a+b
    return sun
print(add(1,2) + add(5,6))

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) #this will combine the two numbers together into a string making it 25

def concatenate(a,b):
    return str(a)+str(b)
print(concatenate(2,5))

#8
def continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    #return 7
print(continents()) # this will print 100, and then because the if statement is not met, it will print the 'else' of 10... the final 'return of 7' is never ran.


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #this will return 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #this will return 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #this will run the first part of the function call and return 7 and then it runs the 2nd half of the function call returning 14, they will be added together summing into 21.


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) #this will run the first return statement of b+c resulting in 8 and then the function is terminated theresfore the second 'return of 10' is never ran.


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b) #This will print out 500, 500, 300, 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b) #this will print out 500, 500, 300, 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b) #this will print out 500, 500, 300, 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()   # i thought it would simply print 1,2,3... But since we defined a function immediately after our 1st print, VS runs that function telling it to print 3, it then is coming back and executing our final print statement of 2 


#15
def foo():
    print(1) #we print 1 initially
    x = bar() #we go down to bar function and immediately print 3 and then thew return value of 5, and then we are printing y which contains the value of 'foo,' meaning whatever we have returned 
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y) #final outlook should be 1,3,5,10

"""


#2
def number_of_military_branches():
    return 5
print(number_of_military_branches())

def countdown(num):
    new_list= []
    for i in range(num, 0, -1):
        new_list.append(i)
    return new_list

print(countdown(5))


#----First Plus Length ------#
# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def firstPlus(list):
    for i in range(len(list)):
        temp = list[0]
    sum = temp + len(list)
    return sum
    
print(firstPlus([4,2,3,4,5]))