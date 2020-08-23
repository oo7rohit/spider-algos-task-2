n = int(input())
for _ in range(n):

    string = input()
    a = 0
    b = 0
    count = 0
    length = len(string)

    for i in range(0, length):
        if string[i] == '<':
            a += 1
        else:
            b += 1

        if b > a:
            print(count)
            break
        else:
            count += 1

        if i == length-1:
            if string[0] != string[count - (a-b) - 1]:
                print(count - (a-b))
            else:
                print(0)

