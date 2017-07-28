#Closures
#This is to see how closures work
##
## More Changes


print("What, No changes?")


def outer_func():
    message = 'hi'

    def inner_func():
        print(message)

    return inner_func

outer_func()
print(dir())

print(outer_func())
print(outer_func)



#print(my_func.__name__)
#inner_func()

#my_func = outer_func()

#print(my_func)
#print(message)
#print(inner_func)
