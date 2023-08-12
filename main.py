
#Calculator in Python programming language

IntOrFloat=input("What type of data do you need? Int or float? ")
if IntOrFloat=="int" or IntOrFloat=="Int":
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    symb=input("Enter symbol (+,-,*,/,// <- division of the whole,^ <- degree of number,%): ")
    if(symb=="+"):
        print(num1,"+",num2,"=",num1+num2,sep="")
    elif(symb=="-"):
        print(num1,"-",num2,"=",num1-num2,sep="")
    elif(symb=="*"):
        print(num1,"*",num2,"=",num1*num2,sep="")
    elif(symb=="/"):
        print(num1,"/",num2,"=",num1/num2,sep="")
    elif symb=="//":
        print(num1,"//",num2,"=",num1//num2,sep="")
    elif symb=="^":
        print(num1,"^",num2,"=",pow(num1,num2),sep="")
    elif symb=="%":
        print(num1,"%",num2,"=",num1%num2,sep="")
    else:
        print("Incorrect character entered")
    del num1,num2,symb
elif IntOrFloat=="float" or IntOrFloat=="Float":
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    symb=input("Enter symbol (+,-,*,/,// <- division of the whole,^ <- degree of number,%): ")
    if symb=="+":
        print(num1,"+",num2,"=",num1+num2,sep="")
    elif symb=="-":
        print(num1,"-",num2,"=",num1-num2,sep="")
    elif symb=="*":
        print(num1,"*",num2,"=",num1*num2,sep="")
    elif symb=="/":
        print(num1,"/",num2,"=",num1/num2,sep="")
    elif symb=="//":
        print(num1,"//",num2,"=",num1//num2,sep="")
    elif symb=="^":
        print(num1,"^",num2,"=",pow(num1,num2),sep="")
    elif symb=="%":
        print(num1,"%",num2,"=",num1%num2,sep="")
    else:
        print("Incorrect character entered")
    del num1,num2,symb
else:
    print("It is necessary to enter int or float.")
del IntOrFloat
