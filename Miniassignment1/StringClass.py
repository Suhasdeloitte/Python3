from itertools import combinations
class StringClass:
    name=0
    lst=[]
    def __init__(self,f):
        self.name=f

    def length(self):
        print(len(self.name))

    def split(self):
       return list(self.name)




obj1=StringClass("12314532")
print(obj1.name)
obj1.length()
lst=obj1.split()
print(lst)


class PairsPossible(StringClass):
    def Pairs(self):
        res=StringClass.split(self)
        grp=2
        pair=[x for x in combinations(res,grp)]
        print(*pair)



obj2=PairsPossible("12314532")
obj2.Pairs()

class SearchCommonElements(StringClass,PairsPossible):
    def Sce(self, st, demo):
        res1 = list(set(st) & set(demo))
        print(res1)

obj3=SearchCommonElements()