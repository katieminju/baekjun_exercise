# 재귀함수 이용하여 팩토리얼 구하기

```N = int(input())
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(N))
```
-----------------------
까지가 정답으로 제출한 코드인데 생각하다보니 for문으로도 만들 수 있을 것 같아서 구글링을 하다가 우연히 팩토리얼을 구하는 다양한 방법을 정리해놓으신 분의 깃을 보게되었다..

## 똑같이 재귀로 구하는 방법인데 코드가 세줄임. 충격.
```def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n>1 else 1
print(factorial_recursive(5))
```

==========================
# 팩토리얼을 구하는 다양한 방법
===================
## 1. math 함수 이용
```import math
print(math.factorial(5))
```
-------------------------------------------------------
## 2. 단순 반복문

```def factorial_for(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret
print(factorial_for(5))
```
-------------------------------------------------------
## 3. reduce 함수
함수형 프로그래밍에서, reduce는 fold라고 일컬어지는 함수 집합의 일원으로 재귀적인 자료구조를 분석하고 주어진 결합 동작을 사용해서 원 자료구조의 부분구조를 반복적으로 처리해 재결합해서 하나의 결과값으로 반환하는 고순위(higher-order) 함수이다.
- For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).

```from functools import reduce
def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n+1))
print(factorial_reduce(5))
```

===============
## 자료출처
* <https://shoark7.github.io/programming/algorithm/several-ways-to-solve-factorial-in-python>