# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*args):                   #* cast into tuples
    sum = 0
    args = list(args)
    args[0] = 0                   #tuples are unchangable
    for i in args:                #must be cast to a list to change
        sum += i                  #can change by using indexes
    return sum

print(add(1,2,3))

#num = (1,2,3)
#for i in num:
 #  print(i)