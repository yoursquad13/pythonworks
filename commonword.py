word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

for i in range(0,len(word1)):
    for j in range(0,len(word2)):
        if word1[i] == word2[j]:
            print(word1[i])
            word1 = word1.replace(word1[i],'.')
