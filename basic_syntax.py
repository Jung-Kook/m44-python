# basic_syntax

print('안녕하세요')
print('저는 홍길동입니다.')
print('만나서 반갑습니다.\n')

# ''' -> 3개룰 이서서 쓰면 줄바꿈 가능
print('''안녕
나는
홍길동''')

# Range
print(range(5))  # => range(0, 5)
for i in range(5):
    print(i, end="")
print("\n")

# List 형변환
print(list)
a = list(range(5))
print(a)  # => [0, 1, 2, 3, 4]

# Range 를 이용한 반복문
for i in range(3):
    print(i)

# List
# 배열이다. 여러개의 멤버변수를 가질 수 있으며 index를 통한 접근이 가능하다. 다른 언어에서는 Array
numbers = [10,9,8,7]
print(numbers[-1])

numbers =[3,1,2]
print(sorted(numbers))  # => [1, 2, 3]
print(numbers.sort())  # => None
print(numbers)  # => [1, 2, 3]

# Dictionary
# Key와 value로 이루어진 자료구조. 다른 언어에서는 map. object 라고도 불린다.
phonebook={
    '중국집': '123-4567',
    '초밥': '987-6543',
    '떡볶이': '1004-1004'
}
print(phonebook['중국집'])  # => 123-4567


