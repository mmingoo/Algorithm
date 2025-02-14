n = int(input())
dict = {}

for _ in range(n):
    name, status = input().split()
    dict[name] = status

    if status == "leave":
        del dict[name]

names = sorted(dict.keys(), reverse=True)
for name in names:
    print(name)