
print('Example 1:')
x = 'saeed'

def my_function1():
    print("My Names is : " + x)

my_function1()

print('Example 2:')

name = 'ali'
def my_function2():
    name='alisa'
    print("Your real name is :"+name)

my_function2()

print("name val is: "+ name)

print('Example 3:')

def global_val_function():
    global y
    y='fantastic'

global_val_function()

print("Python is "+y)


print('Example 4:')

val1 = "awesome"

def myfunc():
  global val1
  val1 = "fantastic"

myfunc()

print("Python is " + val1)