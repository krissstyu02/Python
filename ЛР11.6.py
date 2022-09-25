n=int(input('Введите количество строк='))
stringList=[]
wordDict = dict()

for i in range (n):
    stringList += input().split()

for word in stringList:
    wordDict[word] = wordDict.get(word, 0) + 1

List =[]
for word,i in wordDict.items():
    List.append((-i,word))

sortedList = sorted(List)
for i,word in sortedList:
    print(word)

