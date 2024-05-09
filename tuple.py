"""tuples=("apple","cherry","kiwi")
#print(len(tuple))
#print(tuple)
tuple1=("berry",)
print(type(tuple1))
tuple2=tuple(("cherry",))
print(tuples[2])
x=list(tuples)
x.insert(3,"water melon")
x[0]="orange"
x.remove("cherry")
tuples=tuple(x)

#print(tuples[-3:-1])
print(tuples)"""


t=("apple","cherry","lemon")
(green,red,yellow)=t
#print(green,yellow,red)

#for x in t:
#    print(x)

#i=0
#while i<len(t):
#    print(t[i])
#    i+=1

#for x in range(len(t)):
#    print(t[x])

x=("orange","mango","cherry")
y=t+x
print(y*2)

print(y.count("cherry"))
print(y.index("cherry"))