#Observe and explain why the outputs of sum are completely different.

a="20"
b="30"
c=20
d=30

print(a+b)
print(c+d)

#Outputs are different because a and b are strings and c and d are integers. When we use the + operator on strings, it concatenates them, resulting in "2030". When we use the + operator on integers, it adds them together, resulting in 50.
#In simple words, there is difference of Datatypes.