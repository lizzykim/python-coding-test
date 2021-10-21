
n = int(input())
print(n)

data = list(map(int, input().split(" ")))
count=0
list1 =[]

while True:
  list1=data.sort()
  max = data[n-1]
  n-=max
  count+=1
  if n==0:
    break
print(count)


##############
#최적의 해:
#최대한 많은 그룹을 만들려면,
#작은 수 부터 '현재 모험가 공포도'<= 그룹에 있는 모험가 수(=공포도)일때 그룹 형성 


n= int(input())
data= list(map(int, input().split(" ")))
data.sort() #오름차순으로 정렬 
result=0 #그룹수
count=0 #그룹에 포함된 모험가 수

for i in data: #공포도 낮은것부터 하나씩 확인  
  count+=1 #현재 그룹에 해당 모험가 추가시키기
  if count >=i: #현재 그룹에 모험가 수가 > 현재의 공포도 이상일떄
    result+=1 #그룹 생성
    count=0 #현재 그룹의 모험가 수 초기화
    
print(result)


# 1)길이와 인덱스를 사용하기 보다, list에 데이터를 집어놓고 for i in []: 로 순회해서
#인덱스를 적게 써보기