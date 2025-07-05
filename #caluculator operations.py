#caluculator operations
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
#mathmetical oparators
operator=input('select operatot "+","-","*","/":')
#Adding two variables a and b
if operator == "+"  :
    print(a+b)
#Substracting two variables a and b
elif operator == "-" :
    print(a-b)
#Multiplication of two variables a and b
elif operator == "*" :
    print(a*b)
#Dividing two variables a and b
elif operator == "/" :
    print(a/b)
#selecting invalid operators
else :
    print("invalid operator")