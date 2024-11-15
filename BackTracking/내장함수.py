#sum()
result = sum([1,2,3,4,5])
print("sum:",result)

#min(), max()
min_result  = min(7,3,5,2)
max_result = max(7,3,5,2)

print(f"min_result :{min_result}, max_result: {max_result} ")

#eval()
result  = eval("(3+5)*7")
print("eval:",result)


#sorted()
result = sorted([9,1,8,5,4]) # 오름차순
revers_result = sorted([9,1,8,5,4], reverse = True) # 내림차순
print(f"오름차순 : {result}, 내림차순: {revers_result}")

# sorted() with key
array = [('홍길동', 35), ("이순신", 75), ('아무개, 50')]
result = sorted(array, key = lambda x:x[1], reverse = True)
print(result)

# 순열
from itertools import permutations, combinations
data = ['a','b','c']
permutations_result = list(permutations(data,3))
print(f"순열 결과 : {permutations_result}")

#조합
combinations_result = list(combinations(data,3))
print(f"조합 결과:{combinations_result}")



#Couter
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green','blue','blue'])

print(counter['blue'])
print(counter['red'])
print(dict(counter))

# 최대공약수

import math
def lcm(a,b):
    return a*b // math.gcd(a,b)
a = 21
b = 14

print(math.gcd(21,14)) # 최대공약수
print(lcm(21,14)) # 최소공배수