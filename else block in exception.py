#use of except

try:
    print(20/0)
except ZeroDivisionError:       
    print("hello")
else:
    print("python")


print("---------------------------------\n")

#use of else

print("---------------------------------\n")
try:
    print(20/2)
except ZeroDivisionError:
    print("hello")
else:
    print("python")
