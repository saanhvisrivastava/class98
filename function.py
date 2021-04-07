def countWordsFromFile():
    
    fileName=input("Enter the file name: ")
    numberOfWords=1
    file=open(fileName,"r")
   
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
        print(words)

    print("numberOfWords: ")
    print(numberOfWords)
    

countWordsFromFile()