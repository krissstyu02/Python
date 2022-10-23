class MySet():
    mySet = set()

    def __init__(self, inList):
        self.mySet = set(inList)

    def AddElem(self, element):
        self.mySet.add(element)

    def DelElem(self, element):
        self.mySet.remove(element)

    def Intersec(self, set):
        self.mySet = self.mySet.intersection(set.mySet)

    def Diff(self, set):
        self.mySet = self.mySet.difference(set.mySet)

    def Union(self, set):
        self.mySet = self.mySet.union(set.mySet)


    def print(self): #вывод
        print("Множество:")
        for m in self.mySet:
            print(m)


lis=(1,2,3,4)
Set=MySet(lis) #1 2 3 4
Set.AddElem(6) # 1 2 3 4 6
Set.print()
Set.DelElem(6) # 1 2 3 4
Set.print()
lis2=(1,2,4,6)
Set2=MySet(lis2) # 1 2 4 6
Set.Intersec(Set2) # 1 2 4
Set.print()
Set.AddElem(8) # 1 2  4 8
Set.Diff(Set2) # 8
Set.print()
Set.Union(Set2) #  1 2 4 6 8
Set.print()



