# using lambda

people = [{'name': 'Jack', 'age': 26},
          {'name': 'oha', 'age': 43},
          {'name': 'phal', 'age': 24}
]

#def f(person):
    #return person["name"] ## making a function 

#people.sort(key=f) # making sort from function f

#people.sort(key=f)

#print(people) 


# other method USING LAMABDA


people.sort(key=lambda person: person["age"])
print(people)








