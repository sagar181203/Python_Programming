print("Welcome to plane f2039\nYour plane is cruising at an altitude about 33000ft")
# Taking the input for pilot name 
name=input("Enter your name\n")
# Taking the input for current Altitude
alt=int(input("Please Enter your current Altitude in ft\n"))
print("Captain",name,"your altitude is",alt)
# Checking for the conditions
if(alt==1000):
    print("You can land your plane")
elif(33000>alt>5000):
    print("You have to bring the plane around 5000ft then 1000ft to land the plane")
elif(alt<=5000):
    print("You have to bring the plane around 1000ft to land the plane")
else:
    print("try again! to go lower Altitude for landing")