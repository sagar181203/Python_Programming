#                                              # deleting a string 
# value="hello world"
# del(value)
# print(value)

#                                              # concating the two value using the end  
# value1="hello"
# value2="world"
# print(value1,end=" ")
# print(value2,end=" ")

#                                              # string repetation using the *
# value ="hello world \n"
# print(value*3)

#                                              # check if the substrinmg is present in string
# value="hello world"
# if "Hello".lower() in value:
#     print("hello is present in the string")
# elif"hello" not in value:
#     print("hello is not present in the string")

#                                              # string using the raw string

# value="Are you learning the python? yes\no"
# print(value)

# value_modified=r"Are you learning the python? yes\no"
# print(value_modified)

#                                        # count,index,find ,lower and upper
# value="hello world"
# print(value.count("h"))
# print(value.index("h"))
# print(value.find("h"))
# print(value.lower())
# print(value.upper())

#                                      # iteration through the string
# value="hello" 
# for i in value:
#     print(i)
# for i in range(len(value)):
#     print(value[i])

#                                      # finding the length of a string without using the in built finction
# str="sagar"
# count=0
# for i in str:
#     count+=1
# print("the length of the string=",count)

#                                       # string  silicing
# value="hello world"
# #case 1:start and indexing
# print(value[0:5])
# #case 2:start index
# print(value[6:])
# #case 3:end index
# print(value[:5])
# #case 4:start and end index with step
# print(value[0:5:2])

# # barin twister
# value="tinker"
# print(value[1:4])

#                                       **print the odd indexes of the string in reverse order
# value="tinker"
#           # -2 is for the step which shows the negative or reverse indexing
# print(value[5::-2])


#                               *****   LIST   *****
# value=[1,2,3,4,5,6,7,8,9,10,"hello","world",[1,2,3,4,5,6,7,8,9,10]]

#                                    ***** TUPLE *****
#  VALUE=(1,2,3,4,5,6,7,8,9,10)

# Dictionaries with the name and phone number
#value={"sagar":7272930302,"rahbar":8445554441}

# Dictionaries with json data
# value1={"Name":"sagar","age":19,"address":"India"}
# value2={"Name":"jaimeet","age":19,"address":"India"}
# value3={"Name":"chirag","age":19,"address":"India"}