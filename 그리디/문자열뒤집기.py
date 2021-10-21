#내코드

#내 방법: 전체 0 or 1갯수에서 연속으로 나오는 0,1을 빼준다.
s= input()
# print(s.count("1")) # "1"갯수
# print(s.count("0")) # "0"갯수
count0=0
count1=0

# 0혹은 1이 연속될때 마다 각각 count추가하기
for i in range(len(s)-1):
  if s[i]=="0" and s[i+1]=="0":
    count0+=1
  if s[i]=="1" and s[i+1]=="1":
    count1+=1
# print(count0)
# print(count1)

ans1= s.count("1")-count1
ans0= s.count("0")-count0
print(min(ans1,ans0))
##############
#전부 0으로 바뀌는 경우화 전부 1로 바꾸는 경우중 더 적은 횟수를 가지는 경우를 계산
#0>1 , 1>0으로 변경되는 경우를 확인

data= input()
count0 =0 # 전부 0으로 바꾸는 경우
count1 =0 # 전부 1으로 바꾸는 경우

#첫번째 원소에 대한 처리
if data[0]=='1':
    count0+=1
else:
    count1+=1

#두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
  if data[i] != data[i+1]: #1>0 혹은 0>1로 바뀌는 경우를 다르다 != 로 비교
      # 다음 수에서 1로 바뀔떄
      if data[i+1] =='1':
          count0+=1 #0으로 바꾸는 경우의 수가 하나 증가, 다음 수가 1로 바뀌면 그 수를 0으로 만들어줘야되기때분
      else: #다음수가 0으로 바뀔떄
          count1+=1


print(min(count0,count1)) #바뀌는 수가 적을게 정답