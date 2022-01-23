import sys

def add(x, y) :
    return x + y
f = add      
print(f(10, 20))

print(hex(id(add)))          # 함수 객체의 주소
print(sys.getrefcount(add))  # 함수 객체의 레퍼런스 카운트
print(sys.getsizeof(add))    # 함수 객체의 사이즈



