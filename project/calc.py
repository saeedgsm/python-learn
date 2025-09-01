

def calc():
    
    x=int(input("adad x ra vared kon: \n"))
    y=int(input("adad y ra vared kon: \n"))

    op=input("operator ra vared kon: \n")

    if op == '+':
        result=x+y
    elif op == '-':
        result = x-y
    elif op == '*':
        result = x*y
    elif op == '/':
        result = x/y
    else:
        result = "vorodi eshtebah bod!"

    print("natije vorodi ha shod:" + str(result))


calc()