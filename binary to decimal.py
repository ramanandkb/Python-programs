#convert binary into decimal number
a=int(input("Enter a Binary number: "))
result=0
n=0
while a!=0:
    rem=a%10
    a=a//10
    result=result+rem*(8**n)
    n=n+1
print(result)