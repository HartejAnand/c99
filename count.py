enter=input("Enter anything _____ ")
characterCount=0
wordCount=1
for i in enter:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1
        print("Number of characters in the string: ")
print(characterCount)
print("Number of words in the string: ")
print(wordCount)