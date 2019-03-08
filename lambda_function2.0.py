def myfunction1(n):
    return lambda a:a*n
myfunction2 = myfunction1(2)
a=int(input("Please enter the number whose double you want to check: "))
print(myfunction2(a))
