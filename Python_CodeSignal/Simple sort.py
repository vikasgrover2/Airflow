def solution(arr):

    n = len(arr)
    print(n)
    for i in range(n):
        print("loop " + str(i+1))
        j=0
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
            j+= 1
        print("array now " + str(arr))
    return arr

sol = solution([2,8,4,1,7,5])
print(sol)