def countVowels(word):
    a = word.count('a')
    e = word.count('e')
    i = word.count('i')
    o = word.count('o')
    u = word.count('u')
    vowelcount = a+e+i+o+u

sabda = input('Enter a word: ')

numb = countVowels(sabda)
print(numb)
