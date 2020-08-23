n = int(input())
q = int(input())
arr = list(range(1, n+1))
for _ in range(q):
    l, r, v = [int(n) for n in input().split()]
    arr[l-1] += v
    if r < n:
        arr[r] -= v
my_max = temp = 0
for i in range(n):
    temp += arr[i] - i
    if my_max < temp:
        my_max = temp
print(my_max)
