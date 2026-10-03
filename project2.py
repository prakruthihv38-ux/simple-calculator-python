a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
print("1-addition")
print("2-subtraction")
print("3-multiplication")
print("4-division")
choice=int(input("enter your choice:"))
if choice==1:
    result=a+b
elif choice==2:
    result=a-b
elif choice==3:
    result=a*b
elif choice==4:
    if b==0:
        print("cannot divide by zero")
    else:
        result=a/b
else:
    print("invalid choice")

if choice>=1 and choice<=3:
    print("result:",result)
elif choice==4 and b!=0:
    print("result:",result)
        
