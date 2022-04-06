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
