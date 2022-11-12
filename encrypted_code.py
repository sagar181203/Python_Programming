# First we taking the three input strings
# Number one string is taken as messege string
# Number 2nd and 3rd string is taken as the Encrypted code
string='This is a secret code'
alpha='acegikmoqsuwy'
beta='bdfhjlnprtvxz'
strlist=[]
#looping over string
for i in string:
    gama=0
    if i.lower() in alpha:
        for j in alpha:
            if i.lower()==j:
                strlist.append(beta[gama])
            else:
                gama+=1
    else:
        for j in beta:
            if i.lower()==j:
                strlist.append(alpha[gama])
            else:
                gama+=1
print(string)                
print(' '.join(strlist))                
