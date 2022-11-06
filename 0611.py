# finding seconds in day,week,month,year
seconds_day=60*60*24
print(seconds_day)
seconds_week=seconds_day*7
print(seconds_week)
seconds_month=seconds_day*30
print(seconds_month)
seconds_year=seconds_day*365
print(seconds_year)

"""#using the condition
marks=int(input("enter the marks of students"))
#print(type(marks))
if marks >= 18:
    print("the stuident has passed the exam")
else:
 print("the student has failed the exam")"""

 #designing a simple chatbot using if else condition

print("hello,im chatbot")
print("how may i help you\n")
print("hit1 for software installation request ")
print("hit2 for software update request")
print("hit3 for software uninstall request ")
print("hit4 for software repair request")
print("hit5 for other request ")
#acccepting the user input 
userinput=int(input("enter your choice \n"))
#using if else to process the input 
if userinput==1:
    softwareneeded=input("please provide the software name\n")
elif userinput==2:
    softwareupdate=input("please provide the software name to update\n")
elif userinput==3:
    softwareuninstall=input("please provide the software name to uninstall\n")
elif userinput==4:
    softwarerepair=input("please provide the software name to repair\n")
else:
  otherRequest=input("please provide the details for your request\n")

print("thank you for using our service,our team will getback to you soon")