def max_sum(var1, var2, var3):
    data = [var1, var2, var3]
    max_1 = max(data)
    data.remove(max_1)
    max_2 = max(data)
    sum = max_1 + max_2

    return sum


print(max_sum(4, 2, 9))