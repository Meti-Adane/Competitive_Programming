# Complete the findMedian function below.
def findMedian(arr):
    arr.sort()
    med = (len(arr) // 2)
    return arr[med]