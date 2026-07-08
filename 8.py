happy = ["surya", 21, "gopal", 23]

names={}
numbers={}
stt={}

for i in happy:
   if isinstance(i,str):
    names.append(i)
   else:
    numbers.append(i)

for i in range(len(names)):
    stt[names[i]]=numbers[i]
   
print(names)
print(numbers)
print(stt)
