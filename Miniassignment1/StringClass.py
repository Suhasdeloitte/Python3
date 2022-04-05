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
        return pair



obj2=PairsPossible("12314532")
res1=obj2.Pairs()
print(res1)

class SearchCommonElements(StringClass):
    def Sce(self,a,b):
        a_set=set(a)
        b_set=set(b)

        if len(a_set.intersection(b_set))>0:
            return (a_set.intersection(b_set))

        else:
            return 0






obj3=SearchCommonElements(StringClass)
lst1=['1', '2', '3', '1', '4', '5', '3', '2']
lst2=[('1', '2'), ('1', '3'), ('1', '1'), ('1', '4'), ('1', '5'), ('1', '3'), ('1', '2'), ('2', '3'), ('2', '1'), ('2', '4'), ('2', '5'), ('2', '3'), ('2', '2'), ('3', '1'), ('3', '4'), ('3', '5'), ('3', '3'), ('3', '2'), ('1', '4'), ('1', '5'), ('1', '3'), ('1', '2'), ('4', '5'), ('4', '3'), ('4', '2'), ('5', '3'), ('5', '2'), ('3', '2')]
c=obj3.Sce(lst1,lst2)
print(c)