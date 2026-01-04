x= int(input("enter a number"))
def fact(x):
    if x<=0:
        return 1
    else:
        return x*fact(x-1)
print(fact(x))    


