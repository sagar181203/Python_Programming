import random
counter=0
opt=0
word=["sagar","harsha","gagandeep","rakeenh"]
choosen_word=random.choice(word)
print(" try to guess the word")
print(" the secret word is of length is",len(choosen_word))
while counter<7:
    input_word=input("Answer: ")
    len_in_word=len(input_word)
  
    for i in range(0,len_in_word):
        if choosen_word[i] == input_word[i]:
            opt=opt+1
        else:
            break
    print(opt,"  letters is correct in the word ")

