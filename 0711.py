"""ia1=int(input("enter the ia1 marks\n"))
ia2=int(input("enter the  ia2 marks\n"))
ia3=int(input("enter the  ia3 marks\n"))
print("ia1 marks is",ia1,"\n"  "ia2 marks is", ia2, "\n"  "ia3 marks is",ia3,"\n")
if(ia1>ia2):
    if(ia2>ia3):
      total_marks=ia1+ia2
    else:
        total_marks=ia1+ia3
elif(ia1>ia3):
    total_marks=ia1+ia2
else:
    total_marks=ia1+ia3
avg=total_marks/2
print("the averageof of the best of two is ",avg)"""

"""#FINDING THE SUM OF N WHOLE NUMBER 
endpoint=int(input("enter the value of n\n"))
sum=0
for i in range(endpoint):
  print("the sum is",sum)
  print("i is",i)
  sum=sum+i
print("sum of the first {} natural numbers is {}".format(endpoint,sum))"""

"""# finding the sum of numbers between the given range ( start and end) 
start=int(input("enter the starting point\n"))
end=int(input("enter the end point\n"))
sum=0
for i in range (start,end):
    sum=sum+i
print("sum of the numbers between the {} and {} is {}".format(start,end,sum))"""

"""# finding the sum of n odd numbers in given range 
start=int(input("enter the starting point\n"))
end=int(input("enter the endpoint n\n"))
sum=0
for i in range(start,end,-2):
    print(" the sum is",sum)
    print("i is",i)
sum=sum+i
print("sum of the numbers between the {} and {} is {}".format(start,end,sum))"""

"""# print the number from -10 to -1
for i in range (-10,0,1):
    print(i)"""

""""startpoint=-5
endpoint=-1
for i in range(startpoint,endpoint+1):
     print(i)
else:    
 print("the loop is ended")"""

 # while loop to find the sum of n numbers
end=int(input("enter the endpoint \n"))
sum=0
i=0
while i<=end:
 sum=sum+i
i=i+1
print("sum of the numbers is".format(end,sum))