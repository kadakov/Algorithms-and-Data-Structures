n = int(input())

numbers = [int(i) for i in input().split()]
block_size = int(n ** 0.5)
blocks = []
for i in range(0, n + 1, block_size):
    res = sum(numbers[i:i + block_size])
    blocks.append(res)
k = int(input())

for i in range(k):
    request = [i for i in input().split()]
    request[1], request[2] = int(request[1]), int(request[2])

    if request[0] == 'Add':
        numbers[request[1]] += request[2]
        blocks[request[1] // block_size] += request[2]
    elif request[0] == 'FindSum':
        l, r = request[1] // block_size, (request[2] - 1) // block_size
        res = 0
        if l == r:
            for i in range(request[1], request[2]):
                res += numbers[i]
        else:
            res = sum(numbers[request[1]:(l + 1) * block_size]) + sum(blocks[l + 1: r]) + sum(numbers[r * block_size:request[2]])

        print(res)