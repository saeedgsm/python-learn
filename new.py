name = "saeed"
print(name)
print(type(name))
age = 10
print(type(age),age)

product={
    'name':'book1',
    'weight':1000,
    'price':500,
    'off':2,
}

print(product)
print(type(product))

productToStr=str(product)
print(productToStr)
print(type(productToStr))
print(len(product),len(productToStr))

print('new app line...')
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
input1=int(input("Enter 1st number: "))
print('your entered number is: '+ str(input1) )