import sys
input = sys.stdin.readline
s = list(input().rstrip())
fix_string = ''
stack = []
in_tag = False


for char in s:
    if char == "<":
        while stack:
            fix_string+=stack.pop()

        fix_string += char
        in_tag = True

    elif char == ">":
        fix_string += char
        in_tag = False

    elif char == " ":
        if not in_tag:
            while stack:
                fix_string += stack.pop()
            fix_string += char
        else:
            fix_string += char

    else:
        if in_tag:
            fix_string += char


        elif not in_tag:
            stack.append(char)

while stack:
    fix_string += stack.pop()

print(fix_string)