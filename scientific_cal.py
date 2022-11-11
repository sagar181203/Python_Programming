import math
print("Hello what operration you want to do")
choice1=0
while(choice1 !=4):
    print("choices are")
    print("1.simple single calculation")
    print("2.trignometric values")
    print("3.root")
    print("Press 4 to quit")
    choice1=int(input("Enter the choice\n"))
    
    if(choice1==1):
        # program for simple calculator
        first_num=int(input("enter the first number \n"))
        second_num=int(input("enter the second number \n"))
        print("The first num is ",first_num,"\n","The second num is", second_num )
        print("Operations")
        print("case 1.Addition")
        print("case 2.Substraction")
        print("case 3.Multiplication")
        print("case 4.Divide")
        choice=int(input("enter the choice \n"))
        if(choice==1):
            print("result is",first_num+second_num)
        elif(choice==2):
            print("result is",first_num-second_num)
        elif(choice==3):
            print("result is",first_num*second_num)
        elif(choice==4):
            print("result is",first_num/second_num)
        else:
            print("wrong choice")
     # For trignometric values operation                  
    elif(choice1==2):
        value=float(input("Enter the value for trignometric operations \n"))
        deg=(value*math.pi)/180
        choice2=0
        while(choice2 !=7):
            print("choice")
            print("1.sin")
            print("2.cos")
            print("3.tan")
            print("4.cot")
            print("5.sec")
            print("6.cosec")
            print("press 7 to quit")
            choice2=int(input("Enter the choice\n"))
            if(choice2==1):
             print("The sin value is {}".format(math.sin(deg)))
            elif(choice2==2):   
              print("The cos value is {}".format(math.cos(deg)))
            elif(choice2==3):   
             print("The tan value is {}".format(math.tan(deg)))
            elif(choice2==4):
             print("The cot value is {}".format(math.cot(deg)))
            elif(choice2==5): 
              print("The sec value is {}".format(math.sec(deg)))
            elif(choice2==6):
              print("The cosec value is {}".format(math.cosec(deg)))
    # For Root operation 
    elif(choice1==3):
        value1=int(input("Enter the value"))
        root=math.sqrt(value1)
        print("The root of {} is {}\n".format(value1,root))
    
    