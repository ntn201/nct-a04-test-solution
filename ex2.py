def sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + arr[1:]

def min(arr):
    if len(arr) == 1:
        return arr[0]
    temp = min(arr[1:])
    if temp < arr[0]:
        return temp
    return arr[0]


def max(arr):
    if len(arr) == 1:
        return arr[0]
    temp = max(arr[1:])
    if temp > arr[0]:
        return temp
    return arr[0]

def count(arr,x):
    if len(arr) == 1:
        if arr[0] == x:
            return 1
        return 0
    if arr[0] == x:
        return 1 + count(arr[1:],x)
    return count(arr[1:],x)