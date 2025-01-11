import sys, heapq

input = sys.stdin.readline

n,k = map(int,input().split())
nums = list((input().rstrip()))
stack = []

for num in nums:
    print("num: ", num)
    if not stack:
        stack.append(num)
        print("스택에 추가 : ", stack)
    else:
        while k>0:
            # print("num: ",num + "stack 맨 위:"+stack[-1])
            if num > stack[-1]:
                stack.pop()
                stack.append(num)
                print("스택 pop 후 추가 : ", stack)
                k -= 1
                print("k = ", k)
                break
            else:
                stack.append(num)
                break
    print("-----------------")

print(stack)
if k != 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack[:]))
