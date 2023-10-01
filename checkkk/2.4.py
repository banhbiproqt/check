mystring="DoanNhatTan"
mylist=[1,2,3,4]
mydict={"name":"Tan","age":20,"school":"ptit"}
myset={"a","b","c","a"}
mytuple=("a","b","c")
for item in mylist:
    print(item)
for item in mytuple:
    print(item)
for character in mystring:
    print(character,end='')
for value, key in mydict.items():
    print(key,value)
for value in myset:
    print(value)

