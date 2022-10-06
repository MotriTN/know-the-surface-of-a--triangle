a=float(input("Give a: "))
b=float(input("Give b: "))
c=float(input("Give c: "))
p=(a+b+c)/2
surf=(p*(p-a)*(p-b)*(p-c))**0.5
print("Surface: ",surf,"cm²")