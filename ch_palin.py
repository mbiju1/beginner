#write a program that checks if input is a palindrome or not, ignoring punctuations, commas,etc, not case-sensitive, 
#works for both words and numbers

# ans= input("Input a num to check whether it is a palindrome or not")
# x= int(ans) 
# ans= input("Input a word or sentence to check whether it is a palindrome or not")
# y= str(ans)

#the one where we ourselves input words or sent or nums and they how many of them are palindromes
import os

show_expected_result = False
show_hints = False
def is_palindrome(teststr):
    teststr = teststr.lower() #converts string to all lower case
    #now strip off all punctuations and spaces from string
    newstr= "" 
    for c in teststr:
        if c.isalnum():
            newstr+= c

    #now calcualte the reverse of the string
    reversestr= ""
    strindx= len(newstr)-1 #len resturns length of an object
    while(strindx >=0):  
        reversestr+= newstr[strindx]
        strindx -=1
    
    #so we  get the num/word/sent, remove all punctuaitons and make it into lower case(so it doesnt get confused)
    #then we find it length- 1, since they also start counting from 0
    #then we do a loop at the leng-1 and newstr[strindx] gives the value at the index at the end

    if newstr == reversestr:
         return True
    return False
total = 0
test_words= ["Hello World", "Radar", "Mama?","Madam, I'm Adam", "Race Car"]
for word in test_words:
    total+=is_palindrome(word)
print(total)
