word = input("Enter a word")
reversedword = ""
#print('first: ',word[2],len(word))
 

for i in range(len(word) - 1,-1,-1):
    reversedword = reversedword+word[i]
    #print(word[i])
if reversedword == word:
    print('This is palindrome')
else:
    print('This is not palindrome')
    

