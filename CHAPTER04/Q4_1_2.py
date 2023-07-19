def fid(n):
    result = []
    a = 0
    b = 1
    while a < n:
        result.append(a)
        a = b
        b = a + b
    print(result)
    return result


fid(100)
