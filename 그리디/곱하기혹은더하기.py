#내 코드

s= input()
sum=int(s[0])


for n in range(int(len(s))-1): #왼쪽수 n은 인덱스, 0~3까지만 가면됨
  sum= sum*int(s[n+1])
  if int(s[n])==0 or int(s[n+1])==0: #왜 if 문을 수행문 뒤쪽에다 적어야하는지 고민필요
    sum=sum+int(s[n+1])
print(sum)

##########
#0만 생각하고 1일때 간과함
#최적의 해:
#두 수중 하나라도 1이하면 더하고, 아니면 곱하기

data = input()
result =data[0] #첫 번째 문자를 숫자로 변경하여 대입

for i in range(1,len(data)):
    num = int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num

print(result)

#합계를 첫번째 수로 초기화해준 발상 베리 굿