a=[]
while True:
    b=int(input('''
         1. Push the data onto the stack
         2. Pop the data from the stack
         3.Peek the data from the stack
         4.Display the data from the stack
         5. Exit
         '''))
   # push the data
    if b==1: 
        c=input("Enter the value name")
        a.append(c)
        print(a)
    # pop the data
    if b==2:
        if len(a)==0:
            print("Stack is empty")
        else:
          d=a.pop()
          print(d)
          print(a)
    # peek the data
    if b==3:
        if len(a)==0:
            print("Stack is empty")
        else:
            print("Peek the data from the stack",a[-1])
    # display the data
    if b==4:
        print("Display the data from the stack",a)
    if b==5:
        break
    else:
        print("Invalid input")
        