# 복잡도
a = 5
b = 7
print(a+b)
# O(1)

array = [3, 5, 1, 2, 4]  # 5개의 데이터(N=5)

for i in array:
    for j in array:
        temp = i + j
        print(temp)

for i in range(0, 10):
    print(i)
