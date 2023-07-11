print("LOOP MANIPULATION")
print("Enter FOR for For Loop")
print("Enter WHILE for While Loop")
p=input("Enter Your Choice: ")
if p=="FOR":
    print("Enter 1 for pass statement")
    print("Enter 2 for continue statement")
    print("Enter 3 for break statement")
    print("Enter 4 for all statements")
    n=input("Enter your choice: ")
    a="Prabhat"
    for i in a:
        if n=="1":
            if i=="h":
                pass
            else:
                print(i)
        elif n=="2":
            if i=="h":
                continue
            else:
                print(i)
        elif n=="3":
            if i=="h":
                break
            else:
                print(i)
        elif n == '4':          
            if i=='a':
                pass
            elif i=='t':
                continue                             
            elif i=='k':
                break
            else:
                print(i)
elif p=="WHILE":
    print("Enter 1 for pass statement")
    print("Enter 2 for continue statement")
    print("Enter 3 for break statement")
    print("Enter 4 for all statements")
    k=input("Enter choice: ")
    b = 0
    while b < 15:
        if k == "1":
            if b==10:
                pass
            else:
                print(b)
            b+=1   
        elif k == "2":
            if b==10:
                continue
            else:
                print(b)
            b+=1
        elif k == "3":
            if b==10:
                break
            else:
                print(b)
            b+=1
        elif k == "4":
            if b==2:
                pass
            elif b==3:
                continue
            elif b==5:
                break
            else:
                print(b)
            b+=1
            s=False





