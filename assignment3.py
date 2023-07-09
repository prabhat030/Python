c=0
a=True
while a==True:
    print("MENU:")
    print("Enter 1 for Addition")
    print("Enter 2 for Substraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for Exponentiation")
    print("Enter 6 for Floor Division")
    n = int(input("Enter Your Choice: "))
    num1 = int(input("Enter num 1:"))
    num2 = int(input("Enter num 2:"))
    if n==1:
        c = {num1+num2}
    elif n==2:
        c = {num1-num2}
    elif n==3:
        c = {num1*num2}
    elif n==4:
        c = {num1/num2}
    elif n==5:
        c = {num1**num2}
    elif n==6:
        c = {num1//num2}
    else:
        print("Entered choice is wrong")
    print("Your answer is ",c)
    p=input(print("If you want to continue then press 'y' else press 'n' "))
    if p=='y':
        a=True
    elif p=='n':
        a=False
    
    



