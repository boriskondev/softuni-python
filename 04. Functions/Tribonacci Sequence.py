def tribonacci(num):
    result = [0, 0, 1]
    for i in range(num):
        result.append(sum(result[-3:]))
    return result[2:-1]


trib_num = int(input())

print(" ".join(map(str, tribonacci(trib_num))))