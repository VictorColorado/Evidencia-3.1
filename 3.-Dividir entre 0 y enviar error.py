a=10
b=1

try:
    c = b / a
    print (c)
except (IOError,ZeroDivisionError) as x:
    print ("Error ",x)
else:
    print ("no error")
    
print ("Fin de programa")