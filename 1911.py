##Program for print first n Natural numbers
## Not divisible by 5
#number=0
## taking the intput from user
#end_point=int(input("Enter the end point\n"))
##While loop
#while number<end_point:
#    number+=1
#    if number %5 == 0:
#        continue
#    else:
#        print(number)

#start_point=int(input("Enter the start point\n "))
#end_point=int(input("Enter the end point\n "))
#for i  in range (start_point,end_point+1):
#        if i %12==0:   
#            break
#        else:
#            print(i)

"""                                                        The pass statment                                                      """
#start_point=int(input("Enter the start point\n "))
#end_point=int(input("Enter the end point\n "))
#for i in range (start_point,end_point):
#    pass
#if start_point<end_point:
#    pass
#else:
#    print("Hello!")

# import random
# while True:
#     dice_value_obtained=random.randint(1,6)
#     print(dice_value_obtained)
#     key=input("press any key to continue")

print("\nThe clue for the given question is its a 6 letter word which is synnonym of secret\nclue 2 :its in past tense")
f1="h";f2="hi";half_secret="hid";f4="hidd";f5="hidde"
counter=0
secret_code ="hidden"
while counter<7:
    word=input("Enter the secret code\n")
    counter+=1    
    if word==secret_code:
            print("you have guessed the correct word\n Congratulations!!!")  
            break
    elif(word==f1):
        print("you have guessed the first correct letter of secret code\n try some more turn you still have some turns left")
    elif(word==f2):
        print("you have guessed the first 2 correct letters of secret code")
    elif(word==half_secret):
        print("you have guessed the first 3 correct letters of secret code\n hurry up! you are on half of the way")
    elif(word==f4):
        print("you have guessed the first 4 correct letters of secret code\n hurry up! you are almost there")
    elif(word==f5):
        print("you have guessed the  5 correct letters of secret code\n hurry up! you are almost there")
    else:
        print("better luck next time")
