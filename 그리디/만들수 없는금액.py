#내 코드(손 못댐)
from itertools import combinations


n=input()
print(n)

datas = list(map(int,input().split(" ")))

# for i in range(1,len(n)):
#   print(list(permutations(datas,i)))


print(list(combinations(datas,2)))
print(combinations(datas,2))

##########

n= int(input())
data = list(map(int,input().split(" ")))
data.sort()

target=1
for x in data:
  if target< x:
    break
  target+=x

print(target)