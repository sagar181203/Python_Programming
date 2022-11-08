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