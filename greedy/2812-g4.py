chr_list = list(input().rstrip())
in_tag = False
stack = []
write1 = []

for chr in chr_list:
    if chr == '<':
        in_tag = True
        if stack:
            for _ in range(len(stack)):
                write1.append(stack.pop())

        write1.append(chr)

    elif chr == '>':
        in_tag = False
        write1.append(chr)

    elif chr == ' ':
        if not in_tag:
            for _ in range(len(stack)):
                write1.append(stack.pop())
            write1.append(' ')
        else:
            write1.append(' ')

    else:
        if in_tag:
            write1.append(chr)
        else:
            stack.append(chr)

if stack:
    for _ in range(len(stack)):
        write1.append(stack.pop())

print(''.join(write1))