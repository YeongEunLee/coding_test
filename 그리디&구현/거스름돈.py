n = 1260
array = [500, 100, 50, 10]
count = 0

for coin in array:
  count += n // coin
  n %= coin #n은 coin으로 나눈 나머지 

print(count)