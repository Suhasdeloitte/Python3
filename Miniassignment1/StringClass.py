from itertools import combinations
class StringClass:
    name=0
    lst=[]
    def __init__(self,f): #Constructor Calling
        self.name=f

    def length(self):
        print(len(self.name))

    def split(self):
       return list(self.name)


class PairsPossible(StringClass):
    def Pairs(self):
        res=StringClass.split(self)
        grp=2
        pair=[x for x in combinations(res,grp)]
        return pair

class SearchCommonElements(StringClass):
    def common(self, st, demo):
        a = list(set(st) & set(demo))
        print(a)






obj1=StringClass("12314532") #Parameterized Constructor
print(obj1.name)
obj1.length()
lst=obj1.split()
print(lst)

obj2=PairsPossible("12314532")
res1=obj2.Pairs()
print(res1)

st = input("Enter string to compare ")
obj3 = SearchCommonElements(obj1)
n="12314532"
obj3.common(n, st)
