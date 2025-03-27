lst=[3,3,4,54,5,6,7,87,8,89,9,9,7]
e=[i for i in lst if i%2==0]
print("even lst: " ,e)
o=[i for i in lst if i%2!=0]
print("odd lst: " ,o)
md={str(x):x**2 for x in [3,3,34,45,5,6,7,6,5,3]}
print(md)