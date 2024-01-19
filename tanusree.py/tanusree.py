# python program to make a simple calculator for two numbers.
print("two numbers below")
n=int(input("Enter the first number:"))
a=int(input("Enter the second number:"))
i=1
while i<=10:
    print("1.add",n+a)
    print("1.subtract",n-a)
    print("3.multiply",n*a)
    print("4.divition",n/a)
    break
else:
    i>10
    print("calculation error")