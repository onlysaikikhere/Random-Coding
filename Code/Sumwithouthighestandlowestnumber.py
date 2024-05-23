def sum_array(arr):
    if arr == None or len(arr)<=2 :
        return 0
    else:
        x =min(arr)
        y=max(arr)
        arr.remove(x)
        arr.remove(y)
        return sum(arr)
