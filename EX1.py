#a='SKKU'
#print(a[0]) S가 a의 0으로 대입되있음
#바꿀수가 없다. 정 바꾸려면 a의 문자의 몇번놈을 바꾸는 과정은 아래와 같다.
a = 'SKKU'
b = a.replace('S','G')
c = 3
print(a)
print(b)
#긴 문장의 프린트는 다음과 같이 그냥 변수 출력은 위와 같이 진행
print('I replaced {} to {} {}'.format(a,b,c))
#옛날 같은 경우 이렇게 작성했음
print('I raplaced' + a + 'to' + b + str(c))
#파이썬에서는 허수를 j로 쓴다. 그때 위의 방식으로 쓰면 된다. 파이썬은 어떤 값을 넣느냐에 따라 데이터 타입이 정해진다.
#사칙연산
print(1/3)#리얼 나누기
print(1//3)#몫 계산자 형이 어떻든 간에 다 실수 값으로 계산 정수와 정수의 결과는 정수로 산출되므로 이 값이 0
print(3%2)#나머지 연산자
print(1.0+2)#숫자 형이 다르면 범위가 더 큰 놈으로 캐스팅 그래서 3이아니라 3.0
print(3**2)# 제곱 연산자 삼의 제곱임
# Print('a',end='머머')머머를 맨 마지막에 출력해주는 기능
#\는 이스케이프 문자로서, 그 뒤 문자는 출력하지 말라는 기능
r=r"Hehehe \n"#*3을 써주면 3번 써주게 된다. 그만큼 반복한다는 의미.
print(r)
#변수명은 소문자로 _로 띄어쓰기 대체 변수명 함수명 소문자, 클래스명만 카멜케이스를 써준다.
#상수변수도 대문자로 써준다. ex) PI= 3.14, A=5 그냥 지키면 좋겠다는 약속 권장사항.
i=5
 #print('value is',i)들여쓰기 하나 잘못하면 안된다. 들여쓰기를 통해서 블록 수준을 지정해준다.
print('I repeat, the value is',i)
#a+=1 하면 a에 1을 더한 값을 넣어준다. 라는 의미.
#if 문: if문은 인덴팅이 제일 중요하고 인풋으로 스캔에프의 기능을 한다.  elif와 else로 케이스를 지정해주고,
# 그 케이스들은
number =23
guess =int(input('Enter an integer :'))
if guess == number:
    print ('오롱로올')
elif guess < number:
    print("알랄라라")
else:
    print('핳라하핳')
print('끝')