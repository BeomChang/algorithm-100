# 프로그래밍 문제를 풀다 보면 뒤죽박죽인 N개의 데이터를 숫자의 크기 순으로 0 ~ N-1까지의 숫자로 재정렬 해야되는 경우가 종종 있다.

# 예를 들어 N=5 이고,

# 50 23 54 24 123

# 이라는 데이터가 있다면,

# 2 0 3 1 4

# 가 된다.

# 데이터를 재정렬하는 프로그램을 작성하시오.

def binarySearch(arr, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if target < arr[mid]:
        return(binarySearch(arr, target, start, mid))
    if arr[mid] < target:
        return(binarySearch(arr, target, mid + 1, end))
    if arr[mid] == target:
        return mid


n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
for i in range(n):
    print(binarySearch(sorted_arr, arr[i], 0, len(sorted_arr) - 1), end=' ')