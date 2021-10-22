n,m = map(int,input().split(" "))
result=0

# print(n) 행
# print(m)

for i in range(n):
  data = list(map(int,input().split(" ")))
  minvalue=min(data)
  result = max(result,minvalue) # 처음에는 0이랑 작은 수 비교 해서 큰수를 result로 
  # 그럼 이전에 뽑힌 큰수와, 이번의 작은 수를 또 max로 비교해서 큰수가 result
  #result가 반복되는 것을 확인할것!

print(result)
print("변경")