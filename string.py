# string = """
# salam hadi kefin ,
# hardasan,
# orda hava najurdeh!!
# """
#
# #print(string)
#
# a = "Hello, World!"
# print(a[1])
#
# for x in "banana":
#   print(x)

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("yes")

if "old" not in txt:
    print("no")



print('Slicing Strings .............................')

b = "Hello, World!"
print(b[2:20])

b = "Hello, World!"
print(b[-5:-2])


a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = "Hello, World! erfhywr,uvfh"
print(a.split(","))

age =33
txt = f"The best things in life are free! I am {age} years old."
print(txt)

price = 59.4354785
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = "We are the so-called \nVikings\n from the north."
print(txt,txt.count("n"))