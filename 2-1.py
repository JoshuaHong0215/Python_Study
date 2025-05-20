'''
a = 1.2
print(type(a))
'''
'''
a = 15091
print(type(a))
'''
'''
a = 50
b = 98
print(a + b)
'''
'''
a = 1
b = 2
print(a + b)
'''
'''
a = "Chicken"
b = " is love"
print(a + b)
'''
'''
a = 'I\'m hungry'
print(a)
b = "\"chicken is perfect food\", he say"
print(b)
c = "\"hey get out of hear\", he say"
print(a + b + c)
'''
'''
a = '"교수님 강의 스타일이 너무 별로에요 왜이렇게 전부 두루뭉실하게 말씀하시나요?'
b = ' 교수님 말씀하시는게 정말 하나도 이해가 가지 않아요 제가 뭘 어떻게 해야하죠?", 홍찬호가 말했다.'
print(len(b))
'''
'''
a = '0123456789'
b = a[0:6:2]    # a[ 부터 : 전까지 : 간격 :]로 이해하는게 좋음 따라서, 0부터 6전까지 2칸 간격으로 출력해줘 라고 해석이 됨
print(b)        # 그래서 135가 출력된 것
'''

'''
a = "20250515sunnyday"                                    # 바로 위에 개념의 응용 코드로서, 20250515sunnyday라는 string에 년, 월, 일, 날씨의 개념으로 분류 후 출력한 것임
year = a[0:4]
month = a[4:6]
day = a[6:8]
weather = a[8:]
print(year)
print(month)
print(day)
print(weather)
'''

'''
a = 'i ate %d apple.' % 3
print(a)
b = 'i ate %s apple.' % "three"
print(b)

number = 34
c = 'i ate %d apple' % number
print(c)
'''

'''
a = 'hi'
print(a.upper())
'''

'''
a = 'life is too short'               # .replace를 사용하여 life를 leg로 바꿈
print(a.replace('life', 'leg'))
'''

'''
a = 'I like chicken. It is perfect food in the world'
print(a.replace('chicken', 'stake'))
'''

'''                                   # .split을 사용하여 life is too short라는 문장을 list로 출력
a = 'life is too short'
print(a.split())
'''
'''
a = 'i like chicken. it is perfect food in the world'
b = 'but my mother hate a chicken'
print(a.split())
print(b.split())
'''
'''
number = 2
if int(input(0 % 2 == 0)) :
    print("짝수입니다")
else:
    print("홀수입니다")
'''
money = False
if money:
    print('택시타고 가도 됨')
else:
    print('돈이 없으면 걸어가야지 안그래?')
