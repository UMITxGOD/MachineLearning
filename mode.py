def max(a,b):
    if a>b:
        return a
    return b

arr = ["T","T","F","F","F","F"]
dictnary={}
for i in arr:       #intializing the dict 
    dictnary[i]=0
for i in arr:      #finding values of same occurances
    dictnary[i] +=1
values = dictnary.values()
compareList=list(values)
maximum = 0
for i in range(0,len(compareList),1):
    maximum = max(compareList[i],maximum)
for i in arr:
    if(dictnary[i]==maximum):
        result = i 
        break
print(result)
