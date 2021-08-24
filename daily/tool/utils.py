def arr_add(params=[]) -> None:
    """
    列表引用型
    """
    for i in range(len(params)):
        params[i] += 1

def int_add(param):
    """
    变量
    """
    ++param


arr = [1, 23, 33]
arr_add(arr)
for i in range(len(arr)):
    print(arr[i])

p = 1
int_add(p)
print(p)