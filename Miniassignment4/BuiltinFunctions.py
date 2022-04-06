#Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c

Root = lambda a, b, c, x: (a*(x*x)+b*x+c)

print(Root(3,4,5,2))



#Create a list consisted of the number of occurence of both letters: A and a.

lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
counting_a=list(map(lambda x:x.count("a"),lst1))
counting_A=list(map(lambda x:x.count("A"),lst1))
combination=list(map(lambda x,y:[x,y],counting_a,counting_A))
print(counting_a)
print(counting_A)
print(combination)


#Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.

from functools import reduce

lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
neg_count=list(map(lambda x:x*(-1),
                    filter(lambda x:x<0,lst1)))
print(neg_count)

#Take the first two values, run the function on them. Then take the result and the next value and have a multiplication between them. etc. When no more values are left, return the last result.
multiply = reduce(lambda a, b:a*b , neg_count)
print(multiply)

#Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
mapped = zip(lst1,lst2)
print(list(mapped))